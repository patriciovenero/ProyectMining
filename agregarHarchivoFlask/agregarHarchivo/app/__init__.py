# app/__init__.py
from flask import Flask

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'

# Configurar el directorio de plantillas
app = Flask(__name__, template_folder='templates')

# Importar rutas
from app import routes
