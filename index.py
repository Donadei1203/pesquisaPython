#Importando módulos
from flask import Flask, render_template


#iniciando o App
app = Flask(__name__)


#Criando a primeira rota
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
