# Archivo de conexion a la base de datos en MongoDB
# La base de datos se llama "soporte" (verificalo en Compass)
from pymongo import MongoClient

def conectar():
    try:
        conexion = MongoClient("mongodb://localhost:27017")
        db = conexion["soporte"] #Nombre de la BD
        return db 
    except Exception as e:
        print("Error al conectar con MongoDB: " + e)
        return None
