# Proyecto Urban Grocers 
# Proyecto de Automatización - Urban Grocers API (Sprint 8)

Este proyecto contiene una suite de pruebas automatizadas para validar el comportamiento del campo `name` en el endpoint de creación de kits de productos de la aplicación Urban Grocers.

## 📄 Fuente de Documentación
- La documentación de la API fue consultada a través de la interfaz de **apiDoc** incorporada en el servidor de pruebas (`/docs/`).

## 🛠️ Tecnologías y Técnicas Utilizadas
- **Python 3.x**: Lenguaje de programación base.
- **Pytest**: Framework utilizado para la estructura y ejecución de la suite de pruebas.
- **Requests**: Librería de Python empleada para realizar las solicitudes HTTP (POST) al servidor.
- **Pruebas de Límite y Clases de Equivalencia**: Técnicas de diseño de pruebas aplicadas para determinar los escenarios de validación del campo `name` (0, 1, 511 y 512 caracteres).
- **Aislamiento de Datos**: Uso del método `.copy()` para modificar los diccionarios de prueba sin alterar los datos de origen.

## 🚀 Cómo ejecutar las pruebas
1. Inicia el servidor en la plataforma de TripleTen para obtener la URL activa.
2. Actualiza la variable `URL_SERVICE` en el archivo `configuration.py` con la nueva URL.
3. Abre la terminal en la raíz del proyecto y ejecuta el siguiente comando:
   ```bash
   pytest create_kit_name_kit_test.py