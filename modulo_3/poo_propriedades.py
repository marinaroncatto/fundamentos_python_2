### RESUMO DA SEÇÃO ###

#1. Uma variável de instância é uma propriedade cuja existência depende da criação de um objeto. Todo objeto possui um conjunto diferente de variáveis de instância.
#Além disso, elas podem ser incluídas e removidas livremente de objetos durante seus ciclos de vida. Todas as variáveis de instância de objetos são armazenadas em um dicionário dedicado conhecido como __dict__, contido em todo objeto separadamente.

print()
print("Variável de Instância")
print()

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val
 
    def set_second(self, val):
        self.second = val
 
 
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
 
example_object_2.set_second(3)
 
example_object_3 = ExampleClass(4)
example_object_3.third = 5
 
print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)
 


#2. Uma variável de instância pode ser privada quando seu nome começar com __, mas não esqueça que tal propriedade ainda pode ser acessada de for ada classe usando um nome codificado construído como _ClassName__PrivatePropertyName.

#print(example_object_1._ExampleClass__first)


#3. Uma variável de classe é uma propriedade que existe em exatamente uma cópia e não precisa de nenhum objeto criado para estar acessível. Essas variáveis não são mostradas como conteúdo de __dict__.


print()
print("Variável de Classe")
print()

class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1
 
 
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)
 
print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

#Todas as variáveis de classe de uma classe são armazenadas em um dicionário dedicado chamado __dict__, contido em toda classe separadamente.
print()
print("__dict__")
print()
class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__) 



#4. Uma função chamada hasattr() pode ser usada para determinar se algum objeto ou uma classe contém uma propriedade especificada.

#Por exemplo:
print()
print("Função hasattr()")
print()

class Sample:
    gamma = 0 # Class variable.
    def __init__(self):
 
        self.alpha = 1 # Instance variable.
        self.__delta = 3 # Variável de instância privada.
 
 
obj = Sample()
obj.beta = 2 # Outra variável de instância (que existe somente dentro da instância "obj".)
print(obj.__dict__)
 
#O resultado do código é:
#{'alpha': 1, '_Sample__delta': 3, 'beta': 2}
