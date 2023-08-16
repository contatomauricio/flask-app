from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "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"

historico = []

def terapeuta_resposta(pergunta, historico):
    contexto = "\n".join(historico)
    prompt = f"{contexto}\nUsuário: {pergunta}\nElisa, a terapeuta:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,  # Ajuste este valor conforme necessário
        temperature=0.7  # Ajuste a criatividade da resposta (0.2 - 1.0)
    )
    resposta = response.choices[0].text.strip()
    return resposta

@app.route('/chatbot')  
def terapeuta():
    pergunta = request.args.get('pergunta')
    
    resposta_terapeuta = terapeuta_resposta(pergunta, historico)
    historico.append(f"Usuário: {pergunta}\nElisa: {resposta_terapeuta}")
    
    return jsonify(resposta=resposta_terapeuta)

app.run()
