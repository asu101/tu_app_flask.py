from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

@app.route('/checkConnection', methods=['GET'])
def check_connection():
    server = 'fitbit-lastappppp.database.windows.net'
    database = 'fitbit-lastapp'
    username = 'idrhaAsu@fitbit-lastappppp'
    password = 'VR2RehabVR2'
    driver= '{ODBC Driver 17 for SQL Server}'

    try:
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
            return jsonify({"connection": True})
    except Exception as e:
        return jsonify({"connection": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
