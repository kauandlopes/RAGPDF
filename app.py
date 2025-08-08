from flask import Flask, render_template, request
from main import responder # Certifique-se de que main.py esteja no mesmo diretório ou acessível

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    resposta = None
    # Inicialize pergunta_exibicao para garantir que ela exista mesmo em requisições GET
    pergunta_exibicao = "" 

    if request.method == 'POST':
        pergunta = request.form.get('pergunta') 
        if pergunta:
            try:
                resposta = responder(pergunta) # Chama a função responder do main
                pergunta_exibicao = pergunta # Armazena a pergunta para exibição
            except Exception as e:
                resposta = f"Ocorreu um erro ao processar a pergunta: {e}"
                pergunta_exibicao = pergunta # Ainda exibe a pergunta mesmo com erro
        else:
            resposta = "Por favor, digite uma pergunta."
            pergunta_exibicao = "" # Se a pergunta estiver vazia, não exibe nada

    # Renderiza o template HTML e passa a resposta E a pergunta para o front
    return render_template('index.html', resposta=resposta, pergunta=pergunta_exibicao)

if __name__ == '__main__':
    app.run(debug=True)