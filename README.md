# Proyecto de Conversión de Datos

Este proyecto tiene como objetivo subir archivos ZIP a través de una aplicación web desarrollada en Flask, procesarlos para extraer datos y almacenarlos en MongoDB. Luego, se utiliza un servicio en C# para leer los datos desde Redis, dividirlos en dos colecciones y almacenarlos en MongoDB.

## Pasos para ejecutar el proyecto de Flask

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/proyecto-conversion-datos.git
   ```

2. **Ingresar al directorio del proyecto:**

   ```bash
   cd proyecto-conversion-datos/procesoDeDatos
   ```

3. **Instalar las dependencias del proyecto:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación Flask:**

   ```bash
   python run.py
   ```

5. **Abrir el navegador web:**

   Ve a la dirección `http://localhost:5000` para acceder a la aplicación.

6. **Utilizar el formulario:**

   Utiliza el formulario para subir un archivo ZIP y procesarlo.

## Pasos para ejecutar el servicio en C#

1. **Abrir el proyecto en el IDE:**

   Abre el proyecto en tu IDE de preferencia.

2. **Verificar las dependencias:**

   Verifica que tengas instalados los paquetes `MongoDB.Driver` y `StackExchange.Redis`.

3. **Ejecutar el proyecto:**

   Ejecuta el proyecto desde tu IDE o utilizando el comando `dotnet run`.

4. **Escuchar el servicio:**

   El servicio estará escuchando y procesando datos desde Redis, dividiéndolos en dos colecciones de MongoDB.
