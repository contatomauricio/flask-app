from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = ""

historico = []

def terapeuta_resposta(pergunta, historico):
    contexto = "\n".join(historico)
    prompt = f"{contexto}\nUsuário: {pergunta}\nElisa, a terapeuta:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    resposta = response.choices[0].text.strip()
    return resposta

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def terapeuta():
    pergunta = request.form['pergunta']
    
    resposta_terapeuta = terapeuta_resposta(pergunta, historico)
    historico.append(f"Usuário: {pergunta}\nElisa: {resposta_terapeuta}")
    
    return jsonify(resposta=resposta_terapeuta)

if __name__ == '__main__':
    app.run()

