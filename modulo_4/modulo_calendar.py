## RESUMO DA SEÇÃO ##

#1. No módulo calendar, os dias da semana são exibidos de segunda a domingo. Cada dia da semana tem sua representação na forma de um número inteiro,
#em que o primeiro dia da semana (segunda-feira) é representado pelo valor 0, enquanto o último dia da semana (domingo) é representado pelo valor 6.


#2. Para exibir um calendário para qualquer ano, chame a função calendar com o ano passado como argumento, por exemplo:

import calendar
print(calendar.calendar(2020))
 
#Observação: uma boa alternativa à função acima é a função chamada prcal, que também aceita os mesmos parâmetros da função calendar ,
#mas não requer o uso da função print para exibir o calendário.

import calendar
calendar.prcal(2020)



#3. Para exibir um calendário para qualquer mês do ano, chame a função month , passando o ano e o mês para ela. Por exemplo:


import calendar
print(calendar.month(2020, 9))
 
#Observação: você também pode usar a função prmonth , que tem os mesmos parâmetros da função month ,
#mas não requer o uso da função print para exibir o calendário.


#4. A função setfirstweekday permite alterar o primeiro dia da semana. Ela assume um valor de 0 a 6, em que 0 é domingo e 6 é sábado.

import calendar

calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12)

#5. O resultado da função weekday é um dia da semana como um valor inteiro para um determinado ano, mês e dia:


import calendar
print(calendar.weekday(2020, 9, 29)) # Exibe 1, ou seja, terça-feira.
 

#6. A função weekheader retorna os nomes dos dias da semana em uma forma abreviada.
#O método weekheader requer que você especifique a largura em caracteres para um dia da semana.
#Se a largura fornecida for maior que 3, você ainda obterá os nomes abreviados dos dias da semana consistindo em apenas três caracteres. Por exemplo:


import calendar
print(calendar.weekheader(2)) # Exibe: Mo Tu We Th Fr Sa Su
 

#7. Uma função muito útil disponível no módulo calendar é a função chamada isleap, que, como o nome sugere, permite verificar se o ano é bissexto ou não:


import calendar

print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2021))  # Até, mas sem incluir 2021.

#8. Você pode criar um objeto calendar você mesmo, usando a classe Calendar que, ao criar seu objeto,
#permite que você altere o primeiro dia da semana com o parâmetro opcional firstweekday , por exemplo:


import calendar
 
c = calendar.Calendar(2)
 
for weekday in c.iterweekdays():
    print(weekday, end=" ")
# Resultado: 2 3 4 5 6 0 1
 
#O iterweekdays retorna um iterador para números de dias da semana. O primeiro valor retornado é sempre igual ao valor da propriedade firstweekday .


## LAB   O módulo calendar ##

#Durante este curso, demos uma olhada rápida na classe Calendar . Sua tarefa agora é estender sua funcionalidade com um novo método chamado count_weekday_in_year, que recebe um ano e um dia da semana como parâmetros e, em seguida, retorna o número de ocorrências de um dia da semana específico no ano.

#Use as seguintes dicas:

#Crie uma classe chamada MyCalendar que estende a classe Calendar ;
#Crie o método count_weekday_in_year com os parâmetros year e weekday. O parâmetro weekday deve ser um valor entre 0-6, em que 0 é Segunda-feira e 6 é Domingo. O método deve retornar o número de dias como um número inteiro;
#Na sua implementação, use o método monthdays2calendar da classe Calendar .
#Os seguintes são os resultados esperados:

#Argumentos de amostra

#year=2019, weekday=0

#Resultado esperado

#52


#Argumentos de amostra

#year=2000, weekday=6
#Resultado esperado

#53

print()
print("LAB calendar")
print()
import calendar


class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        current_month = 1
        number_of_days = 0
        while (current_month <= 12):
            for data in self.monthdays2calendar(year, current_month):
                if data[weekday][0] != 0:
                    number_of_days = number_of_days + 1

            current_month = current_month + 1
        return number_of_days

my_calendar = MyCalendar()
number_of_days = my_calendar.count_weekday_in_year(2019, calendar.MONDAY)

print(number_of_days)

