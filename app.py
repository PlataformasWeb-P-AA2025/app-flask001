
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Hola, mundo! Esta app está desplegada en Render usando GitHub Actions. Y esto es una prueba - 3'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
