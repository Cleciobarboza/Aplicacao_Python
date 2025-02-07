# pip install flet
# Tela Inicial
    # Título : Hashzap
    # Botão Inicial Chat
        # quando clicar no botão
        # abrir um poup/modal/alerta
            # Titulo Bem vindo ao Hashzap
            # Caixa de Texto :Escrever seu nome no Chat
            # Botão: Entrar no Chat
                # quando clicar no botão 
                # fechar o popup
                # sumir com o Titulo
                # sumir com o botão Iniciar Chat
                    # carregar o Chat
                    # carregar o campo de enviar mensagem: "Digite sua mensagem"
                    # botão Enviar
                        # quando clicar no botão enviar
                        # enviar a mensagem
                        # limpar a caixa de mensagem

# importar o flet
import flet as ft

# criar uma função principal para rodar o seu aplicativo
def main(pagina):
    # titulo
    titulo = ft.Text("Hashzap")

    # aqui estou criando em tunnel para o chat
    def enviar_mensagem_tunel(mensagem):
        # executar tudo o q eu quero que aconteça para todos os usuários que estão no chat
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe( enviar_mensagem_tunel)     

        # criar uma função para enviar mensagem
    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
   
        # limpar a caixa de mensagem
        campo_enviar_mensagem.value = ""
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat = ft.Column()

    def entrar_chat(evento):
        # fechar o popup
        popup.open = False
        # sumir com o titulo
        pagina.remove(titulo)
        # sumir com o botão iniciar chat
        pagina.remove(botao)
        # carregar o chat
        pagina.add(chat)
        # carregar o campo de enviar mensagem
        pagina.add(campo_enviar_mensagem)   
        # carregar o botão enviar
        pagina.add(linha_enviar)
        # adicionar no chat a mensagem "Fulano entrou no chat"
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.updade()

    # criar popup
        titulo_popup = ft.Text("Bem vindo ao Hashap")
        caixa_nome = ft.TextField(label="Digite o seu nome")
        botao_popup = ft.ElevatedButton("Entrar no Chat")

    popup = ft.AlertDialog(title=titulo_popup, content_padding=caixa_nome, actions=[botao_popup])

    # botao inicial
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.updade()


        botao = ft.ElevatedButton("Iníciar Chat", on_click=abrir_popup)
        # colocar os elementos na página
        pagina.add(botao)
        pagina.add(titulo)

# executar essa função com o flet
ft.app(main, view=ft.WEB_BROWSER)