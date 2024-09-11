from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from preguntasTraumatologia import buscar_respuestas
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Cambia esto por una clave secreta segura

# Leer los códigos permitidos desde el archivo
def cargar_codigos():
    with open('codigos.txt', 'r') as file:
        codigos = file.read().splitlines()
    return codigos

codigos_permitidos = cargar_codigos()

@app.route('/')
def index():
    if 'logged_in' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        codigo = request.form['codigo']
        if codigo in codigos_permitidos:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Código inválido. Por favor, intente de nuevo.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/buscar_respuestas', methods=['POST'])
def buscar():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    pregunta_usuario = request.form['pregunta']
    respuesta = buscar_respuestas(pregunta_usuario)
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)
