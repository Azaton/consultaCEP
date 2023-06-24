import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='D:\\DevOps\\Projetos\\Consultar Livros')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cep = request.form.get('cep')  # Obter o CEP informado no formulário
        if cep:
            try:
                url = f"https://cdn.apicep.com/file/apicep/{cep}.json"
                response = requests.get(url)
                response.raise_for_status()  # Verificar se a solicitação teve sucesso

                data = response.json()
                # Aqui você pode manipular a resposta da API
                # data contém os dados retornados pela API

                return render_template('index.html', data=data)

            except requests.exceptions.RequestException as e:
                return f"Erro na solicitação: {e}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)