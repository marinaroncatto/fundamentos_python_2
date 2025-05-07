## RESUMO DA SEÇÃO ##
#1. Para ler o conteúdo de um arquivo, os seguintes métodos de fluxo podem ser usados:

#read(number) – lê number caracteres/bytes do arquivo e os retorna como uma string; é capaz de ler todo o arquivo de uma só vez;
print()
print(" 1) read()")
print()
from os import strerror

try:
    counter = 0
    stream = open('text.txt', "rt")
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
    

#readline() – lê uma única linha do arquivo de texto;
print()
print(" 2) readline()")
print()
from os import strerror

try:
    character_counter = line_counter = 0
    stream = open('text.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCharacters in file:", character_counter)
    print("Lines in file:     ", line_counter)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    
#readlines(number) – lê number linhas do arquivo de texto; é capaz de ler todo o arquivo de uma só vez;
print()
print(" 3) readlines()")
print()
try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    
#readinto(bytearray) – lê os bytes do arquivo e preenche bytearray com esses dados;
print()
print(" 4) readinto()")
print()
from os import strerror

data = bytearray(10)

try:
    binary_file = open('file.bin', 'rb')
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    
#2. Para gravar novo conteúdo em um arquivo, podemos usar os métodos de fluxo a seguir:

#write(string) – grava uma string em um arquivo de texto;
print()
print(" 5) write(string)")
print()
from os import strerror

try:
	file = open('newtext.txt', 'wt') # Um novo arquivo (newtext.txt) será criado.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
    
#write(bytearray) – grava todos os bytes de bytearray em um arquivo;
print()
print(" 6) write(bytearray)")
print()

from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Seu código que lê bytes a partir do fluxo devem ir aqui.



#3. O método open() retorna um objeto que pode ser usado para iterar por todas as linhas do arquivo dentro de um loop for. Por exemplo:

for line in open("file", "rt"):
    print(line, end='')
 
#O código copia o conteúdo do arquivo no console, linha por linha. Observação: o fluxo fechará a si mesmo automaticamente quando ele atingir o fim do arquivo.

print()
print(" 7) copiando arquivo)")
print()

from os import strerror

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) succesfully written')
src.close()
dst.close()
    
#Vamos analisá-lo:

#linhas 3 a 8: pergunte ao usuário o nome do arquivo a ser copiado e tente abri-lo para leitura; encerre a execução do programa se a abertura falhar; observação: use a função exit() para interromper a execução do programa e passar o código de conclusão para o sistema operacional; qualquer código de conclusão diferente de 0 diz que o programa encontrou alguns problemas; use o valor errno para especificar a natureza do problema;
#linhas 10 a 16: repita quase a mesma ação, mas desta vez para o arquivo de saída;
#linha 18: prepare um pedaço de memória para transferir dados do arquivo de origem para o de destino; essa área de transferência é frequentemente chamada de buffer, daí o nome da variável; o tamanho do buffer é arbitrário – neste caso, decidimos usar 64 kilobytes; tecnicamente, um buffer maior é mais rápido no processo de copiar itens, pois um buffer maior significa menos operações de E/S; na verdade, sempre há um limite, cujo cruzamento não gera mais melhorias; teste você mesmo se quiser.
#linha 19: conte os bytes copiados – este é o contador e seu valor inicial;
#linha 21: tente preencher o buffer pela primeira vez;
#linha 22: desde que você obtenha outro número que não seja zero para os bytes, repita as mesmas ações;
#linha 23: escreva o conteúdo do buffer no arquivo de saída (observação: usamos uma fatia para limitar o número de bytes que estão sendo escritos, já que write() sempre prefere escrever o buffer inteiro)
#linha 24: atualizar o contador;
#linha 25: leia o próximo pedaço de arquivo;
#linhas 30 a 32: limpeza final – o trabalho está feito.


#LAB 1

#Um arquivo de texto contém um texto (nada incomum), mas precisamos saber com que frequência (ou quão raro) cada letra aparece no texto. Essa análise pode ser útil em criptografia, por isso queremos conseguir fazer isso em referência ao alfabeto latino.
#Sua tarefa é criar um programa que:
#pergunta ao usuário o nome do arquivo de entrada;
#lê o arquivo (se possível) e conta todas as letras latinas (letras minúsculas e maiúsculas são tratadas como iguais)
#imprime um histograma simples em ordem alfabética (apenas contagens diferentes de zero devem ser apresentadas)
#Crie um arquivo de teste para o código e verifique se o seu histograma contém resultados válidos.
#Supondo que o arquivo de teste contenha apenas uma linha preenchida com:

#aBc
#samplefile.txt

print()
print(" LAB   Histograma de frequência de caracteres")
print()
from os import strerror

# Inicializa 26 contadores para cada letra do Latim.
# Observação: usamos uma compreensão para isso.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            # Se for uma letra...
            if char.isalpha():
                # ... trataremos como minúscula e atualizaremos o contador apropriado.
                counters[char.lower()] += 1
    file.close()
    # Vamos mostrar os contadores.
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# LAB 2

#O código anterior precisa ser melhorado. Ele está bom, mas precisa melhorar.
#Sua tarefa é fazer algumas alterações, que geram os seguintes resultados:
#o histograma de saída será classificado com base na frequência dos caracteres (o contador maior deve ser apresentado primeiro)
#o histograma deverá ser enviado para um arquivo com o mesmo nome do arquivo de entrada, mas com o sufixo '.hist' (deverá ser concatenado ao nome original)
#Supondo que o arquivo de entrada contenha apenas uma linha preenchida com:

#cBabAa
#samplefile.txt

print()
print(" LAB   Histograma de frequência de caracteres classificados")
print()

from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    file.close()
    file = open(file_name + '.hist', 'wt')
    # Observação: usamos uma lambda para acessar os elementos do diretório e definir inversão para obter uma ordem válida.
    for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
        c = counters[char]
        if c > 0:
            file.write(char + ' -> ' + str(c) + '\n')
    file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

#LAB 3

#O Professor Jekyll dá aulas com os alunos e regularmente faz anotações em um arquivo de texto. Cada linha do arquivo contém três elementos: o primeiro nome do aluno, o sobrenome do aluno e o número de pontos que o aluno recebeu durante determinadas aulas.
#Os elementos são separados por espaços em branco. Cada aluno pode aparecer mais de uma vez dentro do arquivo do Professor Jekyll.
#O arquivo pode ter a seguinte aparência:

#John     Smith    5
#Anna     Boleyn   4.5
#John     Smith    2
#Anna     Boleyn   11
#Andrew   Cox      1.5
#samplefile.txt
    
#Sua tarefa é criar um programa que:

#pede ao usuário o nome do arquivo do Professor Jekyll;
#lê o conteúdo do arquivo e conta a soma dos pontos recebidos por cada aluno;
#imprime um relatório simples (mas classificado), como este:
#Andrew   Cox      1.5
#Anna     Boleyn   15.5
#John     Smith    7.0

#Observação:

#seu programa deve estar totalmente protegido contra todas as falhas possíveis: a inexistência do arquivo, o arquivo vazio ou quaisquer falhas de dados de entrada; encontrar qualquer erro de dados deve causar o encerramento imediato do programa, e o erro deve ser apresentado ao usuário;
#implemente e use sua própria hierarquia de exceções – nós a apresentamos no editor; a segunda exceção deve ser gerada quando uma linha errada for detectada e a terceira quando o arquivo de origem existir, mas estiver vazio.
#Dica: use um dicionário para armazenar os dados dos alunos.    

print()
print("  LAB   Avaliação dos resultados dos alunos")
print()

# Uma classe de exceção base para nosso código:
class StudentsDataException(Exception):
    pass


# Uma exceção para linhas com erro:
class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string


# Uma exceção para um arquivo vazio.
class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)


from os import strerror

# Um dicionário para dados de alunos:
data = { }

file_name = input("Enter student's data filename: ")
line_number = 1
try:
    f = open(file_name, "rt")
    # Ler o arquivo inteiro na lista.
    lines = f.readlines()
    f.close()
    # O arquivo está vazio?
    if len(lines) == 0:
        raise FileEmpty()
    # Varre o arquivo linha por linha.
    for i in range(len(lines)):
        # Chegar até a linha i.
        line = lines[i]
        # Divide em colunas.
        columns = line.split()
        # Devem existir 3 colunas - elas estão lá?
        if len(columns) != 3:
            raise WrongLine(i + 1, line)
        # Cria uma chave a partir do nome e sobrenome do aluno.
        student = columns[0] + ' ' + columns[1]
        # Obter pontos.
        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, line)
        # Atualiza o dicionário.
        try:
            data[student] += points
        except KeyError:
            data[student] = points
    # Imprime os resultados.
    for student in sorted(data.keys()):
        print(student,'\t', data[student])

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
except WrongLine as e:
    print("Wrong line #" + str(e.line_number) + " in source file:" + e.line_string)
except FileEmpty:
    print("Source file empty")
    
