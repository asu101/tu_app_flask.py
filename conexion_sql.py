from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    # Aquí puedes agregar la lógica para obtener datos de la base de datos
    # Por ahora, vamos a devolver un mensaje simple para probar
    return jsonify({"message": "Datos obtenidos con éxito"})

@app.route('/checkConnection', methods=['GET'])
def check_connection():
    try:
        # Reemplaza con tus propios detalles de conexión
        conn = psycopg2.connect(
            host="idrhafitbit-server.postgres.database.azure.com",
            dbname="idrhafitbit-database",
            user="obqiwdgkne",
            password="41ZFD4JF1CA2MZ5J$"
        )
        conn.close()
        return jsonify({"connection": "successful"})
    except Exception as e:
        return jsonify({"connection": "failed", "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
