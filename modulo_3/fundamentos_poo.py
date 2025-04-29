### RESUMO DA SEÇÃO ###

#1. Uma classe é uma ideia (mais ou menos abstrata) que pode ser usada para criar diversas representações; tais representações são conhecidas como objetos.

#2. Quando uma classe é derivada de outra classe, sua relação é chamada de herança. A classe derivada de outra classe é conhecida como subclasse. O outro lado dessa relação é chamado de superclasse. Uma maneira de apresentar essa relação é um diagrama de herança, em que:

#superclasses são sempre apresentadas acima de suas subclasses;
#as relações entre classes são indicadas como setas partindo da subclasse em direção à sua superclasse.

#3. Objetos são equipados com:

#um nome que os identifica e permite fazer a distinção de cada um;
#um conjunto de propriedades (o conjunto pode estar vazio)
#um conjunto de métodos (também pode estar vazio)

#4. Para definir uma classe Python, é necessário usar a palavra-chave class. Por exemplo:


class This_Is_A_Class:
    pass
 

#5. Para criar um objeto da classe definida anteriormente, precisamos usar a classe como se fosse uma função. Por exemplo:


this_is_an_object = This_Is_A_Class()
 
