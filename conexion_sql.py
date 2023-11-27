import psycopg2

cnx = None
try:
    cnx = psycopg2.connect(
        user="obqiwdgkne", 
        password="41ZFD4JF1CA2MZ5J$",
        host="idrhafitbit-server.postgres.database.azure.com", 
        port=5432, 
        database="idrhafitbit-database"
    )
    print("Conexión establecida con éxito.")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
finally:
    if cnx:
        cnx.close()