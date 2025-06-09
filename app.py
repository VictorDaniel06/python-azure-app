from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Nós merecemos um 10 né professor</h1>"

@app.route('/saudacao')
def saudacao():
    return "Bem-vindo à página de saudação!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)
