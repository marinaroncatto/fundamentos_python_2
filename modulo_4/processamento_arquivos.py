### RESUMO DA SEÇÃO ###

#1. Um arquivo precisa ser aberto antes de poder ser processado por um programa e ele deve ser fechado quando o processamento for concluído.

#A abertura do arquivo o associa ao fluxo, que é uma representação abstrata dos dados físicos armazenados na mídia.
#O método de processamento do fluxo é chamado de modo de abertura. Existem três modos de abertura:

#modo de leitura: são permitidas apenas operações de leitura;
#modo de gravação: são permitidas somente operações de gravação;
#modo de atualização: são permitidas tanto leitura quanto gravação.

#2. Dependendo do conteúdo do arquivo físico, podem ser usadas diferentes classes do Python para processar arquivos.
#Em geral, BufferedIOBase é capaz de processar qualquer arquivo, enquanto TextIOBase é uma classe especializada dedicada ao processamento de arquivos de texto
#(ou seja, arquivos que contêm textos visíveis para humanos, divididos em linhas, usando marcadores de nova linha).
#Portanto, os fluxos podem ser divididos em binário e texto.


#3. A sintaxe da função open() é usada para abrir um arquivo:

#open(file_name, mode=open_mode, encoding=text_encoding)

#ex
# stream = open(file, mode = 'r', encoding = None)


#A chamada cria um objeto de fluxo e o associa ao arquivo chamado file_name,
#usando o open_mode especificado e definindo o text_encoding especificado, ou gera uma exceção no caso de erro.

#Vamos analisá-lo:

#o nome da função (open) fala por si só; se a abertura for bem-sucedida, a função retorna um objeto do fluxo, caso contrário, será gerada uma exceção (por ex., FileNotFoundError se o arquivo que você for ler não existir);
#o primeiro parâmetro da função (file) especifica o nome do arquivo que será associado ao fluxo;
#o segundo parâmetro (mode) especifica o modo de abertura usado para o fluxo; é uma string preenchida com uma sequência de caracteres e cada um deles possui seu próprio significado especial (mais detalhes em breve);
#o terceiro parâmetro (encoding) especifica o tipo de codificação (ou seja, UTF-8 quando estiver trabalhando com arquivos de texto)
#a abertura deve ser a primeira operação realizada no fluxo.

#### Abrindo os fluxos: modos ###

#r modo aberto: leitura
#    o fluxo será aberto no modo de leitura;
#    o arquivo associado ao fluxo deve existir e deve ser legível, caso contrário, a função open() gerará uma exceção.

#w modo aberto: gravação
#    o fluxo será aberto no modo de gravação;
#    o arquivo associado ao fluxo não precisa existir; se não existir, será criado; se existir, será truncado para o comprimento zero (apagado); se a criação não for possível (por exemplo, devido a permissões do sistema), a função open() gerará uma exceção.

#a modo aberto: anexação
#    o fluxo será aberto no modo de anexação;
#    o arquivo associado ao fluxo não precisa existir; se não existir, será criado; se existir, o cabeçote de gravação virtual será definido no final do arquivo (o conteúdo anterior do arquivo permanece inalterado).

#r+ modo aberto: leitura e atualização
#    o fluxo será aberto no modo de leitura e atualização;
#    o arquivo associado ao fluxo deve existir e deve ser gravável, caso contrário, a função open() gerará uma exceção;
#    operações de leitura e gravação são permitidas para o fluxo.

#w+ modo aberto: gravação e atualização
#    o fluxo será aberto no modo de gravação e atualização;
#    o arquivo associado ao fluxo não precisa existir; se não existir, será criado; o conteúdo anterior do arquivo permanece inalterado;.
#    operações de leitura e gravação são permitidas para o fluxo.

print("Ex abertura de fluxo")
try:
    stream = open("C:\\Users\\User\\Desktopile.txt", "rt")
    # Processamento fica aqui.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)

#abrimos o bloco try-except porque queremos lidar com erros de tempo de execução suavemente;
#usamos a função open() para tentar abrir o arquivo especificado (observe a maneira que especificamos o nome do arquivo)
#o modo de abertura é definido como texto a ser lido (uma vez que texto é a configuração padrão, podemos ignorar t na string de mode)
#se formos bem sucedido, receberemos um objeto da função open() e o atribuiremos à variável do fluxo;
#caso open() falhe, trataremos a exceção imprimindo toda a informação sobre o erro (é altamente recomendado saber exatamente o que aconteceu)


### Selecionando os modos de texto e binário ###
#Caso exista uma letra b no final da string mode, significa que o fluxo deve ser aberto no modo binário.
#Se a string de modo for encerrada com uma letra t, o fluxo será aberto em modo texto.
#O modo de texto é o comportamento padrão presumido quando nenhum especificador de modo binário/de texto.

#ex: modo leitura
#texto: "rt"
#binario: "rb"

#ex: modo gravação
#texto: "wt"
#binario: "wb"

#ex: modo leitura
#texto: "rt"
#binario: "rb"

#ex: modo anexar
#texto: "at"
#binario: "ab"

#ex: modo leitura e atualização
#texto: "r+t"
#binario: "r+b"

#ex: modo gravação e atualização
#texto: "w+t"
#binario: "w+b"

## Fechamento de Fluxo ##
#Essa ação é realizada por um método chamado de dentro do objeto de abertura de fluxo: stream.close().

#4. Três fluxos predefinidos já estarão abertos na inicialização do programa:

#sys.stdin – entrada padrão;
#sys.stdout – entrada padrão;
#sys.stderr – saída de erro padrão.

#5. O objeto de exceção IOError, criado quando qualquer operação de arquivo falhar (incluindo operações de abertura),
#    contém uma propriedade chamada errno, que contém o código de conclusão da ação com falha. Use esse valor para diagnosticar o problema.

print()
print("Ex: uso do strerror para decifrar o erro identificado por errno")
print()

from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Processamento acontece aqui.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))
