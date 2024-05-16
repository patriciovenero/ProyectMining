from flask import render_template
from pymongo import MongoClient
from io import BytesIO
import zipfile
from data_processor import extract_data, calculate_fourier_transform

@app.route('/mostrar_datos')
def mostrar_datos():
    # Establecer la conexión con MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test']
    collection = db['uploaded_zips']

    # Recuperar el archivo ZIP de MongoDB
    zip_document = collection.find_one({"tipo": "zip"})

    # Obtener el contenido del archivo ZIP
    zip_data = zip_document.get('archivo_zip')

    # Descomprimir el archivo ZIP
    with zipfile.ZipFile(BytesIO(zip_data), 'r') as zip_ref:
        fourier_transforms = []
        for file_name in zip_ref.namelist():
            if file_name.endswith('.TXT'):
                # Obtener los datos del archivo TXT y procesarlos
                data = extract_data(zip_ref, file_name)
                if data:
                    # Calcular la transformada de Fourier si es necesario
                    if 'raw_data' in data and data.get('type') == 'Spectra':
                        fourier_transform = calculate_fourier_transform(data['raw_data'], data.get('sample rate (Hz)'))
                        fourier_transforms.append(fourier_transform)

    # Pasar las transformadas de Fourier a la plantilla HTML para mostrarlas
    return render_template('index.html', fourier_transforms=fourier_transforms)
