from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    # Lógica para obtener datos de la base de datos SQL Server
    return jsonify({"message": "Datos obtenidos con éxito"})

@app.route('/checkConnection', methods=['GET'])
def check_connection():
    try:
        # Reemplaza con tus propios detalles de conexión
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 18 for SQL Server};'
            'SERVER=tcp:fitbit-lastappppp.database.windows.net,1433;'
            'DATABASE=fitbit-lastapp;'
            'UID=idrhaAsu@fitbit-lastappppp;'
            'PWD=VR2RehabVR2;'  # Asegúrate de reemplazar esto con tu contraseña real
            'Encrypt=yes;'
            'TrustServerCertificate=no;'
            
            'Connection Timeout=30;'
        )

        conn.close()
        return jsonify({"connection": "successful"})
    except Exception as e:
        return jsonify({"connection": "failed", "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
