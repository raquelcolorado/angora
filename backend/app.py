import os
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '../database/clientes.db')

# Crear carpeta database si no existe
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Crear tabla si no existe
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    email TEXT,
    pedido TEXT
)
''')
conn.commit()
conn.close()

@app.route('/nuevo-cliente', methods=['POST'])
def nuevo_cliente():
    data = request.json
    nombre = data.get('nombre')
    email = data.get('email')
    pedido = data.get('pedido')

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO clientes (nombre, email, pedido) VALUES (?, ?, ?)',
              (nombre, email, pedido))
    conn.commit()
    conn.close()
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
