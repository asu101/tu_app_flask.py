import subprocess
from flask import Flask, jsonify, request
import pyodbc

app = Flask(__name__)

# Ruta para obtener datos. Aquí deberías implementar la lógica para recuperar datos de tu base de datos.
@app.route('/get_data', methods=['GET'])
def get_data():
    # Lógica para obtener datos de la base de datos SQL Server
    return jsonify({"message": "Datos obtenidos con éxito"})

# Ruta para recibir webhooks. Aquí, podrías ejecutar un script o realizar alguna acción cuando se recibe un POST.
@app.route('/webhook', methods=['POST'])
def webhook():
    subprocess.Popen(["/home/ec2-user/update_app.sh"])
    return 'Webhook recibido'

# Ruta para verificar la conexión a la base de datos.
@app.route('/checkConnection', methods=['GET'])
def check_connection():
    try:
        # Establece conexión con tu base de datos SQL Server usando pyodbc.
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
        return jsonify({"connection": "successful"})
    except Exception as e:
        return jsonify({"connection": "failed", "error": str(e)})

# Ruta para insertar datos en la base de datos.
@app.route('/insert_data', methods=['POST'])
def insert_data():
    data = request.json
    try:
        # Conexión con la base de datos para realizar la inserción.
        conn = pyodbc.connect(
            # Cadena de conexión
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
        # Ejecuta el comando SQL para insertar datos.
        cursor.execute("INSERT INTO TestTable (Edad, ID, Nombre) VALUES (?, ?, ?)",
                       data['Edad'], data['ID'], data['Nombre'])
        conn.commit()
        return jsonify({"message": "Datos insertados con éxito"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/insert_actividad_alejandro_saiz', methods=['POST'])
def insert_actividad_alejandro_saiz():
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

            cursor.execute("""
                INSERT INTO ActividadesAlejandroSaiz (
                    Fecha,
                    BreathingRate,
                    ECGData,
                    HeartRate,
                    HRV,
                    LifetimeStats,
                    SleepLog,
                    SpO2,
                    VO2Max,
                    DailyActivitySummaryResponse,
                    PersonaID
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                           data['Fecha'],
                           data['BreathingRate'],
                           data['ECGData'],
                           data['HeartRate'],
                           data['HRV'],
                           data['LifetimeStats'],
                           data['SleepLog'],
                           data['SpO2'],
                           data['VO2Max'],
                           data['DailyActivitySummaryResponse'],
                           data['PersonaID']
                           )

            conn.commit()
            return jsonify({"message": "Actividad de Alejandro insertada con éxito"})
        except Exception as e:
            return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

