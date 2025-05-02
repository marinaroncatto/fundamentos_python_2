## RESUMO DA SEÇÃO ##
#1. Um método é uma seção integrada em uma classe. O primeiro (ou único) parâmetro de cada método geralmente é chamado self, projetado para identificar o objeto para qual o método foi chamado para acessar as propriedades objeto ou chamar seus métodos.

print()
print("Ex 1: parâmetro self")
print()
class Classy:
    def method(self):
        print("method")


obj = Classy()
obj.method()


print()
print("Ex 2: mais de um parâmetro")
print()

class Classy:
    def method(self, par):
        print("method:", par)
 
 
obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)


print()
print("Ex 3: self chamando outros métodos de dentro da classe")
print()


class Classy:
    def other(self):
        print("other")
 
    def method(self):
        print("method")
        self.other()
 
 
obj = Classy()
obj.method()

#2. Se uma classe contiver um construtor (um método chamado __init__) ela não pode retornar nenhum valor e não pode ser chamada diretamente.

print()
print("Ex 4: __init__")
print()

class Classy:
    def __init__(self, value):
        self.var = value


obj_1 = Classy("object")

print(obj_1.var)

print()
print("Ex 4: __init__ com argumento padrão")
print()

class Classy:
    def __init__(self, value = None):
        self.var = value


obj_1 = Classy("object")
obj_2 = Classy()

print(obj_1.var)
print(obj_2.var)

print()
print("Ex 4: método privado")
print()    

class Classy:
    def visible(self):
        print("visible")
 
    def __hidden(self):
        print("hidden")
 
 
obj = Classy()
obj.visible()
 
try:
    obj.__hidden()
except:
    print("failed")
 
obj._Classy__hidden()
 
    

#3. Todas as classes (mas não os objetos) contêm uma propriedade chamada __name__, que armazena o nome da classe. Além disso, uma propriedade chamada __module__ armazena o nome do módulo em que a classe foi declarada, enquanto a propriedade chamada __bases__ é uma tupla que contém as superclasses de uma classe.

#Por exemplo:
print()
print("Ex 5: __name__")
print()

class Sample:
    def __init__(self):
        self.name = Sample.__name__
    def myself(self):
        print("My name is " + self.name + " living in a " + Sample.__module__)
 
 
obj = Sample()
obj.myself()
#O resultado do código é:
#My name is Sample living in a __main__



#Se quiser descobrir a classe de um objeto específico, use a função type(), capaz de (entre outras coisas) descobrir uma classe que foi usada para instanciar qualquer objeto.

print()
print("Ex 6: função type()")
print()
class Classy:
    pass

print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)


#__module__ também é uma string, ela armazena o nome do módulo que contém a definição da classe.

print()
print("Ex 7: __module__")
print()

class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)
#Como você sabe, qualquer módulo chamado __main__ na verdade não é um módulo, mas o arquivo em execução no momento.

#__bases__ é uma tupla. A tupla contém classes (e não nomes de classe) que são superclasses diretas para a classe.
#A ordem é a mesma usada dentro da definição da classe.
#Mostraremos apenas um exemplo básico, uma vez que queremos destacar como funciona a herança.
#Além disso, iremos mostrar como usar esse atributo quando discutimos os aspectos da abordagem por objetos das exceções.
#Observação: somente classes possuem este atributo, objetos não.

print()
print("Ex 8: __bases__")
print()

class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)
    

 
## LAB 1 CLASSE TIMER##

#Sua classe será chamada Timer. Seu construtor aceita três argumentos representando horas (um valor no intervalo [0..23], usaremos o sistema de 24 horas), minutos (no intervalo [0..59]) e segundos (intervalo [0..59]).
#Zero é o valor padrão para todos os parâmetros acima. Não há necessidade de se realizar verificações de validação.
#A própria classe deve oferecer os seguintes recursos:
#objetos da classe devem ser "imprimíveis", ou seja, devem ser capazes de converter a si mesmos de maneira implícita em strings no seguinte formato: "hh:mm:ss", com zeros à esquerda incluídos quando qualquer um dos valores for menor de 10;
#a classe deve ser equipada com métodos sem parâmetro chamado next_second() e previous_second(), incrementando o tempo armazenado dentro dos objetos por +1/-1 segundo, respectivamente.
#Use as seguintes dicas:

#todas as propriedades do objeto devem ser privadas;
#recomendamos escrever uma função separada (e não um método!) para formatar a string de hora.

print()
print("Lab 1 - Classe timer")
print()
def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return two_digits(self.__hours) + ":" + \
               two_digits(self.__minutes) + ":" + \
               two_digits(self.__seconds)

    def next_second(self):
        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes > 59:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours > 23:
                    self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

## LAB 2 - Dias da semana ##

#Sua tarefa é implementar uma classe chamada Weeker. Não, seus olhos não estão lhe enganando, a origem deste nome é o fato dos objetos dessa classe serem capazes de armazenar e manipular os dias da semana (ou days of the week, em inglês).
#O construtor da classe aceita um argumento: uma string. A string representa o nome do dia da semana, em inglês, e os únicos valores aceitáveis devem vir do seguinte grupo:

#Mon Tue Wed Thu Fri Sat Sun

#Chamar o construtor com um argumento que não esteja presente nesse grupo irá gerar a exceção WeekDayError (defina-a você mesmo; não se preocupe, falaremos sobre a natureza objetiva das exceções em breve). A classe deve fornecer os seguintes recursos:
#objetos da classe devem ser "imprimíveis", ou seja, devem ser capazes de converter a si mesmos de maneira implícita em strings no mesmo formato dos argumentos do construtor;
#a classe deve ser equipada com métodos de um parâmetro, chamados add_days(n) e subtract_days(n), sendo n um número inteiro que atualiza o dia da semana armazenado dentro do objeto, refletindo a mudança da data pelo número de dias indicado, seja a mais ou a menos.
#todas as propriedades do objeto devem ser privadas;
print()
print("Lab 2 - Dias da semana")
print()

class WeekDayError(Exception):
    pass


class Weeker:
    __names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.__names[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + n) % 7

    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")


##Lab 3 - pontos em um plano ##

#Cada ponto localizado no plano pode ser descrito como um par de coordenadas normalmente conhecidas como x e y. Queremos que você crie uma classe Python que armazene ambas as coordenadas como números float. Além disso, queremos que os objetos dessa classe avaliem as distâncias entre dois planos situados no plano.
#A tarefa é bastante simples se usarmos a função chamada hypot() (disponível no módulo math), que avalia o comprimento da hipotenusa de um triângulo direito (mais detalhes aqui: https://pt.wikipedia.org/wiki/Hipotenusa) e aqui: https://docs.python.org/pt-br/3.7/library/math.html#trigonometric-functions.
#É assim que imaginamos a classe:
#ela é chamada Point;
#seu construtor aceita dois argumentos (x e y respectivamente), ambos com padrão zero;
#todas as propriedades devem ser privadas;
#a classe contém dois métodos sem parâmetros chamados getx() e gety(), que retornam as duas coordenadas (as coordenadas são armazenadas de maneira privada, portanto não podem ser acessadas diretamente a partir de dentro do objeto);
#a classe fornece um método chamado distance_from_xy(x,y), que calcula e retorna a distância entre o ponto armazenado dentro do objeto e o outro ponto fornecido como um par de valores flutuantes;
#a classe fornece um método chamado distance_from_point(point), que calcula a distância (como o método anterior), mas o local do outro ponto é fornecido como outro objeto da classe Point;

print()
print("Lab 3 - pontos em um plano")
print()
import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))

## Lab 4 - triângulo ##

#Agora iremos integrar a classe Point (veja o Lab 3.4.1.14) dentro de outra classe. Além disso, iremos colocar três pontos em uma classe, que irá permitir a definição de um triângulo. Como podemos fazer isso?
#A nova classe será chamada Triangle e é isto que queremos:
#o construtor aceita três argumentos, todos eles objetos da classe Point;
#os pontos são armazenados dentro do objeto como uma lista privada;
#a classe oferece um método sem parâmetros chamado perimeter(), que calcula o perímetro do triângulo descrito pelos três pontos; o perímetro é a soma de todos os comprimentos dos catetos (mencionamos isso apenas para fins informativos, mas temos certeza que você já sabe disso.)
#Preencha o modelo que fornecemos no editor. Execute seu código e confirme se o parâmetro avaliado é o mesmo que o nosso.

print()
print("Lab 4 - triângulo")
print()
import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        per = 0
        for i in range(3):
            per += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
        return per


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())

