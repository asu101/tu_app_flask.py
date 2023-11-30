import subprocess
from flask import Flask, jsonify, request
import pyodbc

app = Flask(__name__)


@app.route('/get_data', methods=['GET'])
def get_data():
    # Lógica para obtener datos de la base de datos SQL Server
    return jsonify({"message": "Datos obtenidos con éxito"})

@app.route('/webhook', methods=['POST'])
def webhook():
    subprocess.Popen(["/home/ec2-user/update_app.sh"])
    return 'Webhook recibido'


@app.route('/checkConnection', methods=['GET'])
def check_connection():
    try:
        # Reemplaza con tus propios detalles de conexión
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 18 for SQL Server};'
            'SERVER=tcp:fitbit-lastappppp.database.windows.net,1433;'
            'DATABASE=fitbit-lastapp;'
            'UID=idrhaAsu@fitbit-lastappppp;'
            'PWD=VR2RehabVR2;'
            'Encrypt=yes;'
            'TrustServerCertificate=no;'

            'Connection Timeout=30;'
        )

        conn.close()
        return jsonify({"connection": "successful - prueba 0.2"})
    except Exception as e:
        return jsonify({"connection": "failed", "error": str(e)})


@app.route('/insert_data', methods=['POST'])
def insert_data():
    data = request.json
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 18 for SQL Server};'
            'SERVER=tcp:fitbit-lastappppp.database.windows.net,1433;'
            'DATABASE=fitbit-lastapp;'
            'UID=idrhaAsu@fitbit-lastappppp;'
            'PWD=VR2RehabVR2;'
            'Encrypt=yes;'
            'TrustServerCertificate=no;'
            'Connection Timeout=30;'
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TestTable (Edad, ID, Nombre) VALUES (?, ?, ?)",
                       data['Edad'], data['ID'], data['Nombre'])
        conn.commit()
        return jsonify({"message": "Datos insertados con éxito"})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

