import os
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, render_template, redirect, url_for, request, session
from datetime import datetime

# Inicializa o Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Defina uma chave secreta para a sessão

@app.route('/')
def home():
    # Verifica se o usuário está logado
    if 'user' in session:
        notas_ref = db.collection('notes').stream()
        notas = [{'titulo': nota.to_dict()['title'],
                  'conteudo': nota.to_dict()['content'],
                  'data_criacao': nota.to_dict()['createdAt']} for nota in notas_ref]
        return render_template('home.html', user=session['user'], notas=notas)
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_success', methods=['POST'])
def login_success():
    user_data = request.json  # Dados do Firebase enviados via POST
    session['user'] = user_data['user']
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/nova-nota', methods=['GET', 'POST'])
def nova_nota():
    if request.method == 'POST':
        titulo = request.form['titulo']
        conteudo = request.form['conteudo']
        data_criacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Adiciona a nova nota ao Firestore
        doc_ref = db.collection('notes').add({
            'title': titulo,
            'content': conteudo,
            'createdAt': data_criacao
        })
        return redirect(url_for('home'))
    
    return render_template('nova_nota.html')

if __name__ == '__main__':
    app.run(debug=True)
