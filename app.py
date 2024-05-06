from flask import Flask, render_template, request
from preguntasTraumatologia import buscar_respuestas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar_respuestas', methods=['POST'])
def buscar():
    pregunta_usuario = request.form['pregunta']
    respuesta = buscar_respuestas(pregunta_usuario)
    return respuesta

if __name__ == '__main__':
    app.run(debug=True)