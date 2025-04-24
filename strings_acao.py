### RESUMO DA SEÇÃO ###

#1. Strings podem ser comparadas com outras strings usando operadores de comparação gerais, mas compará-las com número não retorna resultados lógicos, pois nenhuma string pode ser igual a qualquer número. Por exemplo:

#string == number será sempre False;
#string != number será sempre True;
#string >= number sempre retornará uma exceção.

#2. Ordenar listas de strings pode ser feito da seguinte maneira:

#uma função chamada sorted(), criando uma nova lista ordenada;
print("Demonstrando a função sorted():")
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()


#um método chamado sort(), que ordena a lista in situ
print("Demonstrando o método sort():")
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)


#3. Um número pode ser convertido em string por meio da função str() .
print("Conversão número para string: ")
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)
    
#4. Uma string pode ser convertida em um número (no entanto, nem toda string) por meio da função int() ou float() . A conversão irá falhar caso uma string não contenha uma imagem de número válido (será lançada uma exceção).
print("Conversão String para número: ")
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)
    


### LAB ###

#Sua tarefa é criar um programa capaz de simular um dispositivo com sete displays, mas você irá usar LEDs individuais em vez de segmentos.
#Cada dígito é construído por 13 LEDs (algumas acesas, outras não, é claro); é desta maneira que o imaginamos:

digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]


def print_number(num):
	global digits
	digs = str(num)
	lines = [ '' for lin in range(5) ]
	for d in digs:
		segs = [ [' ',' ',' '] for lin in range(5) ]
		ptrn = digits[ord(d) - ord('0')]
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):
			lines[lin] += ''.join(segs[lin]) + ' '
	for lin in lines:
		print(lin)


print_number(int(input("Enter the number you wish to display: ")))
