from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint 1: Verificación de estado
@app.route('/check', methods=['GET'])
def check():
    return "API #2 is working", 200

# Endpoint 2: Retornar JSON
@app.route('/', methods=['GET'])
def get_info():
    return jsonify({
        "Instancia": "Instancia #2 - API #2",
        "Curso": "Seminario de Sistemas I",
        "Seccion": "Sección A",
        "Periodo": "2do Semestre 2024",
        "Estudiante": "Denis Augusto Coronado Calderón - 202101499"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)