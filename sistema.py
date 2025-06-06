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

#Funcion que elimina un equipo de la coleccion
def eliminarEquipo():
    db = conectar()
    if db is None:
        print("No se pudo conectar a la DB ❌ ")
        return

    coleccion = db["equipos"]
    print("\n--- 🗑️ Eliminar un equipo 🗑️ ---")
    modelo = input("Ingresa modelo del equipo a eliminar: ").strip()
    equipo = coleccion.find_one({"modelo": modelo})
    if equipo:
        respuesta = input(f"Deseas eliminar el equipo {modelo} "
                          f"del cliente {equipo.get('cliente')}? (s/n)"
                          )
        if respuesta == "s":
            coleccion.delete_one({"_id": equipo["_id"]})
            print("✔️  El equipo ha sido eliminado")
        else:
            print("❌  Operación cancelada")
    else:
        print("⚠️ No se encontro un equipo con ese modelo")


def agregarReparacion():
    db = conectar()
    if db is None:
        print("No se pudo conectar a la BD ❌ ")
        return
    coleccion = db["reparaciones"] #Aqui cambia el nombre la colección
    print("--- 📄 Registro de reporte de reparación 📄 ---")
    cliente = input("Nombre del cliente: ").strip()
    modelo = input("Modelo del equipo: ").strip()
    problema = input("Problema encontrado: ").strip()
    solucion = input("Solución de reparación: ").strip()
    fecha = input("Fecha de reparación: ").strip()
    costo = float(input("Costo de la reparación $ "))
    nuevaReparacion = {
        "cliente": cliente,
        "modeloEquipo": modelo,
        "problema": problema,
        "solucion": solucion,
        "fecha": fecha,
        "costo": costo
    }
    registro = coleccion.insert_one(nuevaReparacion)
    print(f"\n✔️  Reporte registrado con el ID {registro.inserted_id}")


def mostrarReparaciones():
    db = conectar()
    if db is None:
        print("No se pudo conectar a la BD ❌ ")
        return
    coleccion = db["reparaciones"] #Aqui cambia el nombre la colección
    reparaciones = coleccion.find()
    print("\n--- 📝 Lista de Reparaciones Registradas 📝---")
    for r in reparaciones:
        print(f"Cliente: {r.get('cliente')} - Modelo: {r.get('modeloEquipo')}"
              f"Problema detectado: {r.get('problema')} - "
              f"Solución ejecutada: {r.get('solucion')} - "
              f"Fecha de reparacion: {r.get('fecha')} - Costo ${r.get('costo')}"
              )


def eliminarReparacion():
    db = conectar()
    if db is None:
        print("No se pudo conectar a la BD ❌ ")
        return
    coleccion = db["reparaciones"] #Aqui cambia el nombre la colección
    print("--- 🗑 Eliminar una orden de reparación 🗑 ---")   
    modelo = input("Ingresa modelo del equipo en reparación a eliminar: ")
    equipo = coleccion.find_one({"modeloEquipo": modelo})
    if equipo:
        respuesta = input(f"Deseas eliminar la orden de reparacion del equipo {modelo} "
                          f"del cliente {equipo.get('cliente')}? (s/n)"
                          )
        if respuesta == "s":
            coleccion.delete_one({"_id": equipo["_id"]})
            print("✔️  La orden de reparación ha sido eliminada")
        else:
            print("❌  Operación Cancelada")
    else:
        print("⚠️  No se encontro una orden de reparación para ese modelo")


#MENU DE OPCIONES (Esto se ejecuta por default)
while True:
    print("\n--- 💻 Taller de Soporte y Mantenimiento 💻 ---")
    print("1. Agregar nuevos equipos")
    print("2. Mostrar equipos registrados")
    print("3. Eliminar un equipo registrado")
    print("4. Agregar reporte de reparacion")
    print("5. Listado de reparaciones registradas")
    print("6. Eliminar orden de reparacion")
    print("9. Salir del sistema")

    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        agregaEquipo()
    if opcion == "2":
        mostrarEquipos()
    if opcion == "3":
        eliminarEquipo()
    if opcion == "4":
        agregarReparacion()
    if opcion == "5":
        mostrarReparaciones()
    if opcion == "6":
        eliminarReparacion()
    if opcion == "9":
        print("\nAdios! 👋 ")
        break