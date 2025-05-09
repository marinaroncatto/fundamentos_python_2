## RESUMO DA SEÇÃO ##
#1. Para criar um objeto date , você deve passar os argumentos year, month e day da seguinte forma:

from datetime import date
 
my_date = date(2020, 9, 29)
print("Year:", my_date.year) # Ano: 2020
print("Month:", my_date.month) # Mês: 9
print("Day:", my_date.day) # Dia: 29
 
#O objeto date tem três atributos (somente leitura): year, month e day.


#2. O método today retorna um objeto de data que representa a data local atual:

from datetime import date
print("Today:", date.today()) # Exibe: Today: 2020-09-29
 

#3. No Unix, o timestamp expressa o número de segundos desde 1º de janeiro de 1970, 00h00min00s (UTC).
#Essa data é chamada de "época Unix", porque começou a contagem do tempo em sistemas Unix.
#O timestamp é, na verdade, a diferença entre uma data específica (incluindo o tempo) e 1º de janeiro de 1970, 00h00min00s (UTC),
#expressa em segundos. Para criar um objeto de data a partir de um timestamp, precisamos passar um timestamp Unix para o método fromtimestamp :

from datetime import date
import time
 
timestamp = time.time()
d = date.fromtimestamp(timestamp)

#Observação: a função time retorna o número de segundos de 1º de janeiro de 1970 até o momento atual na forma de um número flutuante.

#4. O construtor da classe time aceita seis argumentos (hour, minute, second, microsecond, tzinfo e fold). Cada um desses argumentos é opcional.


from datetime import time
 
t = time(13, 22, 20)
 
print("Hour:", t.hour) # Hour: 13
print("Minute:", t.minute) # Minute: 22
print("Second:", t.second) # Second: 20
 

#5. O módulo time contém a função sleep , que suspende a execução do programa por um determinado número de segundos, por exemplo:


import time
 
time.sleep(10)
print("Hello world!") # Este texto será exibido após 10 segundos.
 

#6. No módulo datetime, data e hora podem ser representadas como objetos separados ou como um único objeto.
#A classe que combina data e hora é chamada datetime.
#Todos os argumentos passados ao construtor vão para atributos de classe somente leitura.
#São eles year, month, day, hour, minute, second, microsecond, tzinfo e fold:


from datetime import datetime
 
dt = datetime(2020, 9, 29, 13, 51)
print("Datetime:", dt) # Exibe: Datetime: 2020-09-29 13:51:00
 

#7. O método strftime recebe apenas um argumento na forma de uma string, especificando um formato que pode consistir em diretivas.
#Uma diretiva é uma string que consiste no caractere % (porcentagem) e uma letra minúscula ou maiúscula. A seguir estão algumas diretrizes úteis:

#%Y – retorna o ano com o século como um número decimal;
#%m – retorna o mês como um número decimal com zeros;
#%d – retorna o dia como um número decimal preenchido com zeros;
#%H – retorna a hora como um número decimal com zeros;
#%M – retorna o minuto como um número decimal com zeros;
#%S – retorna o segundo como um número decimal com zeros.
#Exemplo:

from datetime import date
 
d = date(2020, 9, 29)
print(d.strftime('%Y/%m/%d')) # Exibe: 2020/09/29
 

#8. É possível executar cálculos em objetos date e datetime, por exemplo:


from datetime import date
 
d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)
 
d = d1 - d2
print(d) # Exibe: 366 days, 0:00:00.
print(d * 2) # Exibe: 732 days, 0:00:00.
 

#O resultado da subtração é retornado como um objeto timedelta que expressa a diferença em dias entre as duas datas no exemplo acima.
#Observe que a diferença em horas, minutos e segundos também é exibida. O objeto timedelta pode ser usado para cálculos posteriores (por exemplo, você pode multiplicá-lo por 2.


# LAB   Os módulos datetime e time #

#Escreva um programa que crie um objeto datetime para 4 de novembro de, 14h53min00s. O objeto criado deve chamar o método strftime com o formato apropriado para exibir o seguinte resultado:

#2020/11/04 14:53:00
#20/November/04 14:53:00 PM
#Wed, 2020 Nov 04
#Wednesday, 2020 November 04
#Weekday: 3
#Day of the year: 309
#Week number of the year: 44

#Observação: cada linha de resultado deve ser criada chamando o método strftime com pelo menos uma diretiva no argumento format.

from datetime import datetime

my_date = datetime(2020, 11, 4, 14, 53)

print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
print(my_date.strftime("%a, %Y %b %d"))
print(my_date.strftime("%A, %Y %B %d"))
print(my_date.strftime("Weekday: %w"))
print(my_date.strftime("Day of the year: %j"))
print(my_date.strftime("Week number of the year: %W"))
    
