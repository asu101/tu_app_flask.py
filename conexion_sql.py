from flask import Flask, jsonify
import pymssql

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    # Lógica para obtener datos de la base de datos SQL Server
    return jsonify({"message": "Datos obtenidos con éxito"})

@app.route('/checkConnection', methods=['GET'])
def check_connection():
    try:
        # Reemplaza con tus propios detalles de conexión
        conn = pymssql.connect(
            server='fitbit-lastappppp.database.windows.net',
            user='idrhaAsu@fitbit-lastappppp',
            password='VR2RehabVR2',
            database='fitbit-lastapp',
            port=1433
        )

        conn.close()
        return jsonify({"connection": "successful"})
    except Exception as e:
        return jsonify({"connection": "failed", "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
