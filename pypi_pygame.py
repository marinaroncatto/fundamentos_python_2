import pygame

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
  for event in pygame.event.get():
   if event.type == pygame.QUIT\
   or event.type == pygame.MOUSEBUTTONUP\
   or event.type == pygame.KEYUP:
    run = False

### RESUMO DA SEÇÃO ###
#1. Existe um repositório (ou repo, abreviado) criado para coletar e compartilhar código Python gratuito, conhecido como Python Package Index (PyPI), embora também seja provável que você ouça um nome extremamente específico, The Cheese Shop. O website do Shop está disponível em https://pypi.org/.


#2. Para usar o The Cheese Shop, foi criada uma ferramenta especializada, conhecida como pip (pip instala pacotes enquanto pip significa... ok, deixa pra lá). Como o pip não pode ser implementado como parte da instalação padrão do Python, é possível que você precise instalá-lo manualmente. O pip é uma ferramenta de console.


#3. Para verificar a versão do pip, emita um dos seguintes comandos:

#pip --version
 
#ou

#pip3 --version
 
#Confirme por conta própria qual desses funcionam no ambiente de seu SO.


#4. A lista das atividades principais do pip são semelhantes às seguintes:

#pip help operação – mostra uma breve descrição do pip;
#pip list – mostra uma lista dos pacotes instalados atualmente;
#pip show nome_pacote – mostra a info do nome_pacote incluindo as dependências do pacote;
#pip search anystring – busca os diretórios do PyPI por pacotes cujos nomes contenham anystring;
#pip install nome – instala nome em todo o sistema (é esperado que ocorram problemas caso você não tenha direitos administrativos);
#pip install --user nome – instala nome somente para você; nenhum outro usuário da plataforma conseguirá usá-lo;
#pip install -U nome – atualiza um pacote instalado anteriormente;
#pip uninstall nome – desinstala um pacote instalado anteriormente.
