from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="¡Hola mundo, tarea num 6!")

if __name__ == '__main__':
    app.run()
