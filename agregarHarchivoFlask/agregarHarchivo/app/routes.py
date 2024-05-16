# app/routes.py
from flask import render_template, request, jsonify
import os
import redis
from . import app

# Configuración de Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para subir el archivo ZIP y enviarlo a Redis
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and file.filename.endswith('.zip'):
        file_data = file.read()
        r.set('uploaded_zip', file_data)
        return jsonify({'message': 'File uploaded successfully'}), 200
    return jsonify({'error': 'Invalid file format, must be a .zip file'}), 400

