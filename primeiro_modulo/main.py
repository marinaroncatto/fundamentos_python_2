from sys import path
 
path.append('..∖∖modules')

#Como a barra invertida é usada de escape para outros caracteres, caso queira só uma barra invertida, é necessário usar o caractere de escape.
#usamos o nome relativo da pasta, isto irá funcionar caso você use o arquivo main.py diretamente de sua pasta inicial, e não irá funcionar se o diretório atual não se encaixar no caminho relativo; você pode usar um caminho absoluto, como este:
#path.append('C:\\Users\\user\\py\\modules')
#usamos o método append(); na verdade, o novo caminho ocupará o último elemento na lista de caminhos. Se você não gostar dessa ideia, basta usar insert() no lugar.

from module import suml, prodl
 
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

#import sys

#for p in sys.path:
#    print(p)



######## RESUMO DA SEÇÃO ##########

#1. Embora um módulo seja projetado para agrupar algumas entidades relacionadas como funções, variáveis ou constantes, um pacote é um contêiner que permite o agrupamento de diversos módulos relacionados sob um nome comum. Tal contêiner pode ser distribuído em seu estado atual (como um lote de arquivos implementados em uma subárvore de diretório) ou pode ser compactado em um arquivo zip.


#2. Durante a primeira importação do módulo em si, o Python converte seu código fonte em um formato semicompilado armazenado nos arquivos pyc e implementa esses arquivos no diretório __pycache__ localizado no diretório inicial do módulo.


#3. Caso queira avisar o usuário do seu módulo que uma entidade específica deve ser tratada como privada (ou seja, não deve ser usada fora do módulo de maneira explícita), é possível marcar o nome com os prefixos _ ou __. Não se esqueça que essa é apenas uma recomendação, e não uma exigência.


#4. Os nomes shabang, shebang, hashbang, poundbang e hashpling descrevem o dígrafo escrito como #!, usado para instruir SOs similares a Unix como o arquivo fonte do Python deve ser iniciado. Essa convenção não tem nenhum efeito no MS Windows.


#5. Caso queira convencer o Python que ele deve levar em consideração o diretório de um pacote não padrão, seu nome precisa ser inserido/anexado na/à lista de diretórios de importação armazenada na variável path presente no módulo sys.


# 6. Um arquivo Python chamado __init__.py é executado de maneira implícita quando um pacote que o contém estiver sujeito a importação, e é utilizado para inicializar um pacote e/ou seus subpacotes (caso existam). O arquivo pode ficar vazio, mas não pode estar ausente.
