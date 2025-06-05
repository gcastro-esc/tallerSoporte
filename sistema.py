#Archivo sistema, mostrara un menu de acciones
#contendra las funciones necesarias
from conexion import conectar

#Funcion que agrega equipos a la BD
def agregaEquipo():
    db = conectar()
    if db is None:
        print("No se pudo conectar a la BD ❌ ")
        return
    
    coleccion = db["equipos"] #Nombre de la coleccion
    print("\n--- 💻 Registro de nuevo equipo 💻 ---")
    cliente = input("Nombre del cliente: ").strip()
    marca = input("Marca del equipo: ").strip()
    modelo = input("Modelo del equipo: ").strip()
    sistema = input("Sistema Operativo: ").strip()
    estado = input("Estado al ingreso: ").strip()

    nuevoEquipo = { #Los campos deben coincidir con la coleccion en MongoDB
        "cliente": cliente,
        "marca": marca,
        "modelo": modelo,
        "sistemaOperativo": sistema,
        "estado": estado
    }

    registro = coleccion.insert_one(nuevoEquipo)
    print(f"\n✔️  Equipo registrado con el ID {registro.inserted_id}")


#Funcion que lista todos los equipos registrados en la coleccion
def mostrarEquipos():
    db = conectar()
    if db is None:
        print("No se pudo conectar a la DB ❌ ")
        return

    coleccion = db["equipos"]
    equipos = coleccion.find()
    print("\n--- 💻 Lista de Equipos Registrados 💻 --- ")
    for x in equipos:
        print(f"Cliente: {x.get('cliente')} - Marca: {x.get('marca')} - "
              f"Modelo: {x.get('modelo')} - "
              f"Sistema Operativo: {x.get('sistemaOperativo')} - "
              f"Estado: {x.get('estado')}"
              )


#MENU DE OPCIONES (Esto se ejecuta por default)
while True:
    print("\n--- 💻 Taller de Soporte y Mantenimiento 💻 ---")
    print("1. Agregar nuevos equipos")
    print("2. Mostrar equipos registrados")

    print("9. Salir del sistema")
    
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        agregaEquipo()
    if opcion == "2":
        mostrarEquipos()

    if opcion == "9":
        print("\nAdios! 👋 ")
        break