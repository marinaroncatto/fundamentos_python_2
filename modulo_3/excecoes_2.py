### RESUMO DA SEÇÃO ###
#1. A ramificação else: da instrução try é executado quando não houver acontecido nenhuma exceção durante a execução do bloco try:.
print()
print("1) ramificação else(bloco try)")
print()

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n


print(reciprocal(2))
print(reciprocal(0))
    

#2. A ramificação finally: da instrução try sempre será executada.
print()
print("2) ramificação finally(bloco try)")
print()

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n


print(reciprocal(2))
print(reciprocal(0))
    

print()
print("## anatomia das exceções ##")
print()

def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)

#3. A sintaxe except Exception_Name como um exception_object: permite que você intercepte um objeto carregando informações sobre uma exceção pendente. A propriedade do objeto chamada args (uma tupla) armazena todos os argumentos transmitidos para o construtor do objeto.
print()
print("3) exept Exception_name")
print()
def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ' ,end=' : ')
    print_args(e.args)

try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)
    
#4. As classes de exceção podem ser estendidas para aprimorá-las com novos recursos ou adotar suas características em novas exceções definidas.
print()
print("4) 1")
print()

try:
        assert __name__ == "__main__"
except:
        print("fail", end=' ')
else:
        print("success", end=' ')
finally:
        print("done")
 

#O resultado do código é: success done.


print()
print("4) Exception personalizada")
print()

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
                
