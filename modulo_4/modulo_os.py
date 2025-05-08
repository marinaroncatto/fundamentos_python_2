
### RESUMO DA SEÇÃO ###

#1. A função uname retorna um objeto que contém informações sobre o sistema operacional atual. O objeto possui os seguintes atributos:

#systemname (armazena o nome do sistema operacional)
#nodename (armazena o nome da máquina na rede)
#release (armazena a versão do sistema operacional)
#version (armazena a versão do sistema operacional)
#machine (armazena o identificador de hardware, por exemplo x86_64).

#import os
#print(os.uname()) #funciona em linux
# saída esperada: posix.uname_result(sysname='Linux', nodename='192d19f04766', release='4.4.0-164-generic', version='#192-Ubuntu SMP Fri Sep 13 12:02:50 UTC 2019', machine='x86_64')

#Infelizmente, a função uname só funciona em alguns sistemas Unix. Se você usa Windows, pode usar a função uname no módulo platform, que retorna um resultado semelhante.

#2. O atributo name disponível no módulo os permite distinguir o sistema operacional. Ele retorna um dos três valores a seguir:

#posix (você obterá esse nome se usar Unix)
#nt (você obterá esse nome se usar o Windows)
#java (você obterá esse nome se seu código for escrito em algo como Jython)
import os
print(os.name)


#3. A função mkdir cria um diretório no caminho passado como seu argumento. O caminho pode ser relativo ou absoluto, por exemplo:

import os
 
os.mkdir("hello") # caminho relativo
os.mkdir("/home/python/hello") # caminho absoluto
 
#Observação: se o diretório existir, uma exceção FileExistsError será lançada. Além da função mkdir , o módulo os fornece a função makedirs ,
#que permite criar recursivamente todos os diretórios em um caminho.

import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())

#4. O resultado da função listdir() é uma lista que contém os nomes dos arquivos e diretórios que estão no caminho passado como argumento.

#É importante lembrar que a função listdir omite as entradas '.' e '..', que são exibidas, por exemplo, ao usar o comando ls -a em sistemas Unix.
#Se o caminho não for passado, o resultado será retornado para o diretório de trabalho atual.

#5. Para mover entre diretórios, você pode usar uma função chamada chdir(), que altera o diretório de trabalho atual para o caminho especificado.
#Como argumento, ele toma qualquer caminho relativo ou absoluto.

#Se você quiser descobrir qual é o diretório de trabalho atual, você pode usar a função getcwd() , que retorna o caminho para ele.

import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())
    

#6. Para remover um diretório, você pode usar a função rmdir() mas para remover um diretório e seus subdiretórios, use a função removedirs() .

import os

os.mkdir("my_first_directory")
print(os.listdir())
os.rmdir("my_first_directory")
print(os.listdir())


#7. Tanto no Unix quanto no Windows, você pode usar a função do sistema, que executa um comando passado a ela como uma string, por exemplo:


import os
 
returned_value = os.system("mkdir hello")
 
#A função do sistema no Windows retorna o valor retornado pelo shell após a execução do comando fornecido, enquanto Unix retorna o status de saída do processo.


#LAB

#Seu programa deve atender aos seguintes requisitos:

#Escreva uma função ou método chamado find que receba dois argumentos chamados path e dir. O argumento path deve aceitar um caminho relativo ou absoluto para um diretório onde a pesquisa deve começar, enquanto o argumento dir deve ser o nome de um diretório que você deseja encontrar no caminho fornecido. Seu programa deve exibir os caminhos absolutos se encontrar um diretório com o nome fornecido.
#A pesquisa de diretório deve ser feita recursivamente. Isso significa que a pesquisa também deve incluir todos os subdiretórios no caminho fornecido.
print()
print("LAB o módulo os")
print()
import os

class DirectorySearcher:
    def find(self, path, dir):
        try:
            os.chdir(path)
        except OSError:
            # Não processa um arquivo que não seja um diretório.
            return

        current_dir = os.getcwd()
        for entry in os.listdir("."):
            if entry == dir:
                print(os.getcwd() + "/" + dir)
            self.find(current_dir + "/" + entry, dir)


directory_searcher = DirectorySearcher()
directory_searcher.find("./tree", "python")
    
