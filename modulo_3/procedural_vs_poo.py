### RESUMO DA SEÇÃO ###

#1. Uma pilha é um objeto criado para armazenar dados por meio do modelo LIFO. A pilha geralmente realiza pelo menos duas operações, chamadas de push() e pop().


#2. A implementação da pilha em um modelo procedural gera uma série de problemas que podem ser resolvidos pelas técnicas oferecidas pela POO (Object Oriented Programming, ou Programação Orientada a Objetos).


#3. Um método de classe é na verdade uma função declarada dentro da classe e capaz de acessar todos os componentes da classe.


#4. A parte da classe Python responsável por criar novos objetos é chamada de construtor e é implementada como um método de nome __init__.


#5. Cada declaração de método de classe deve conter pelo menos um parâmetro (sempre o primeiro), geralmente conhecido como selfe é usado pelos objetos para identificar a si mesmos.


#6. Se quisermos ocultar qualquer um dos componentes de uma classe do mundo exterior, o nome deve começar com __. Esses componentes são chamados de privados.


## LAB 1 ##

#Recentemente, mostramos estender as possibilidades da Pilha ao definir uma nova classe (ou seja, uma subclasse) que retém todas as características herdadas, além de incluir algumas novas.

#Sua tarefa é estender o comportamento da classe Stack de maneira que a classe seja capaz de contar todos os elementos enviados por push e pop (presumimos que a contagem de pops é o suficiente). Use a classe Stack que fornecemos no editor.

#Siga as dicas:

#introduza uma propriedade criada para contar operações de pop e nomeie-a de maneira que assegura que ela fique oculta;
#inicialize-a como zero dentro do construtor;
#forneça um método que retorna o valor atribuído atualmente ao contador (nomeie-o get_counter()).
#Complete o código no editor. Execute-o para confirmar se o resultado é 100.

print("Lab Pilha de contagem")
print()

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def pop(self):
        self.__counter += 1
        return Stack.pop(self)


stk = CountingStack()
for i in range(100):
    stk.push(i) 
    stk.pop()
print(stk.get_counter())


## LAB 2 ""

#Como você já sabe, uma pilha é uma estrutura de dados que segue o modelo LIFO (último a entrar, primeiro a sair). É algo simples e ao qual você já deve estar totalmente acostumado.

#Vamos tentar algo novo. Uma fila é um modelo de dados caracterizado pelo termo FIFO: primeiro a entrar, primeiro a sair. Observação: uma fila comum que você vê em mercados ou no correio funcionam exatamente da mesma maneira: o cliente que chegou primeiro também é atendido primeiro.

#Sua tarefa é implementar a classe Queue com duas operações básicas:

#put(element), que coloca um elemento no fim da fila;
#get(), que pega um elemento da frente da fila e o retorna como o resultado (a fila não pode estar vazia para que isso tenha sucesso.)
#Siga as dicas:

#use uma lista como armazenamento (como fizemos com a pilha)
#put() deve anexar elementos ao início da lista, enquanto get() deve remover os elementos do fim da lista;
#defina uma nova exceção chamada QueueError (escolha uma exceção da qual derivá-la) e gere-a quando get() tentar realizar operações em uma lista vazia.
#Complete o código fornecido no editor. Execute-o para verificar se o seu resultado é semelhante ao nosso.

print()
print(" LAB   Fila ou FIFO")
print()

class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")

## LAB 2 parte 2 ##

#Sua tarefa é ampliar a capacidade da classe Queue . Queremos que ela tenha um método sem parâmetro que retorne True caso a fila esteja vazia e False quando não estiver.
#Complete o código fornecido no editor. Execute-o para verificar se o seu resultado é semelhante ao nosso.
#Se desejar, copie o código abaixo, que usamos no lab anterior:

print()
print(" LAB   Fila ou FIFO: parte 2")
print()

class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []
    def put(self,elem):
        self.queue.insert(0,elem)
    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError


class SuperQueue(Queue):
    def isempty(self):
        return len(self.queue) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Fila vazia")
