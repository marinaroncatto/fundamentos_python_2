## RESUMO DA SEÇÃO ##

#1. Um método chamado __str__() é responsável por converter o conteúdo de um objeto em uma string legível (a grosso modo). Você pode redefini-la se quiser que seu objeto seja capaz de apresentar a si mesmo de forma mais elegante. Por exemplo:

print()
print("1) __str__()")
print()
class Mouse:
    def __init__(self, name):
        self.my_name = name
 
 
    def __str__(self):
        return self.my_name
 
 
the_mouse = Mouse('mickey')
print(the_mouse) # Prints "mickey".
 

#2. Uma função chamada issubclass(Class_1, Class_2) é capaz de determinar se Class_1 é uma subclasse de Class_2. Por exemplo:

print()
print("2) issubclass")
print()

class Mouse:
    pass
 
 
class LabMouse(Mouse):
    pass
 
 
print(issubclass(Mouse, LabMouse), issubclass(LabMouse, Mouse)) # Prints "False True
 

#3. Uma função chamada isinstance(Object, Class) verifica se um objeto é proveniente de uma classe indicada. Por exemplo:

print()
print("3) isinstance")
print()

class Mouse:
    pass
 
 
class LabMouse(Mouse):
    pass
 
 
mickey = Mouse()
print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse)) # Prints "True False".
 

#4. Um operador chamado is verifica se duas variáveis se referem ao mesmo objeto. Por exemplo:

print()
print("4) is")
print()
class Mouse:
    pass
 
 
mickey = Mouse()
minnie = Mouse()
cloned_mickey = mickey
print(mickey is minnie, mickey is cloned_mickey) # Prints "False True".
 

#5. Uma função sem parâmetro chamada super() retorna uma referência à superclasse mais próxima da classe. Por exemplo:

print()
print("5) super()")
print()

class Mouse:
    def __str__(self):
        return "Mouse"
 
 
class LabMouse(Mouse):
    def __str__(self):
        return "Laboratory " + super().__str__()
 
 
doctor_mouse = LabMouse();
print(doctor_mouse) # Prints "Laboratory Mouse".
 

#6. Métodos, bem como variáveis de classe e de instância definidas em uma superclasse são herdadas automaticamente por suas subclasses. Por exemplo:

print()
print("6) hierarquia")
print()
class Mouse:
    Population = 0
    def __init__(self, name):
        Mouse.Population += 1
        self.name = name
 
    def __str__(self):
        return "Hi, my name is " + self.name
 
class LabMouse(Mouse):
    pass
 
professor_mouse = LabMouse("Professor Mouser")
print(professor_mouse, Mouse.Population) # Prints "Hi, my name is Professor Mouser 1"
 

#7. Para encontrar qualquer propriedade de objeto/classe, o Python procura por ela:

#no próprio objeto;
#em todas as classes envolvidas na linha de herança do objeto, de baixo para cima;
#caso exista mais de uma classe em um caminho de herança específico, o Python faz uma varredura da esquerda para direita;
#se os métodos acima falharem, a exceção AttributeError será gerada.

#8. Se alguma das subclasses definem um método, variável de classe ou variável de instância do mesmo nome na superclasse, o novo nome substitui as instâncias anteriores do mesmo nome. Por exemplo:

print()
print("8) substituição (overriding)")
print()

class Mouse:
    def __init__(self, name):
        self.name = name
 
    def __str__(self):
        return "My name is " + self.name
 
class AncientMouse(Mouse):
    def __str__(self):
        return "Meum nomen est " + self.name
 
mus = AncientMouse("Caesar") # Prints "Meum nomen est Caesar"
print(mus)
 
