import numpy as np
from scipy.fft import fft

def extract_data(zip_ref, file_name):
    """
    Extrae los datos relevantes de un archivo TXT en un archivo ZIP.
    Retorna un diccionario con la información extraída.
    """
    data = {}
    with zip_ref.open(file_name, 'r') as file:
        lines = file.readlines()

        # Analizar las líneas para extraer los datos relevantes
        # Aquí debes implementar la lógica para analizar las líneas y extraer la información necesaria
        # Ejemplo:
        data['type'] = lines[3].split('=')[1].strip()  # Tipo de datos (Spectra o Waveform)
        data['raw_data'] = [float(line) for line in lines[9:] if line.strip() and not line.startswith('data follows')]  # Datos crudos (sin encabezados ni líneas vacías)
        # Otros campos como location, axis, range, units, etc.

    return data

def calculate_fourier_transform(raw_data, sample_rate):
    """
    Calcula la transformada de Fourier de los datos dados.
    Retorna una lista de tuplas (frecuencia, valor_transformada).
    """
    # Calcular la transformada de Fourier usando SciPy
    n = len(raw_data)
    yf = fft(raw_data)
    xf = np.linspace(0.0, 1.0 / (2.0 * sample_rate), n // 2)

    # Obtener solo la parte positiva de la transformada
    yf_pos = 2.0 / n * np.abs(yf[:n // 2])

    # Emparejar las frecuencias con los valores transformados
    fourier_transform = list(zip(xf, yf_pos))

    return fourier_transform
