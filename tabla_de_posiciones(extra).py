equipos = {} #diccionario asi cada equipo tiene un puntaje "Equipo1 : 6 pts"

print("--------- Bienvenido al torneo de futbol ---------")

print() 

while True:
    print("1. Agregar equipo")
    print("2. Registrar resultado")
    print("3. Mostrar tabla")
    print("4. Eliminar un equipo")
    print("5. Finalizar")

    print()
    opcion = input("Seleccione una opcion: ")

    match opcion:
        case "1":
            print("Eligió la opcion 1 a continuacion ingrese la informacion requerida.")
            nombre = input("Ingrese el nomre del equipo: ")
            if(nombre in equipos):
                print("El equipo ya existe. Por favor ingrese uno nuevo.")
                continue
            else:
                equipos[nombre] = 0
                print("El equipo fue agregado con exito...")
        case "2":
            print("Eligió la opcion 2 a continuacion ingrese la informacion requerida.")
            local = input("Equipo local: ")
            visitante = input("Equipo visitante: ")
            if local == visitante:
                print("Esta ingresando los mismos equipos tanto para local como para visitante. Intente otra vez.")
                print()
                continue
            marcador = input("Ingrese marcador(ej : 4-2): ")

            if local not in equipos or visitante not in equipos:
                print("Uno de los equipos no existe.")
                continue

            if "-" not in marcador:
                print("Formato no valido")
                continue
            
            goles = marcador.split("-")

            goles_local = int(goles[0])
            goles_visitante = int(goles[1])
            
            if(goles_local > goles_visitante):
                equipos[local] += 3
            elif (goles_local < goles_visitante):
                equipos[visitante] += 3
            else:
                equipos[local] += 1
                equipos[visitante] += 1

        case "3":
            ordenados = sorted(equipos.items(), key= lambda x: x[1], reverse=True)

            for equipo, puntos in ordenados:
                print(equipo, "-", puntos, "pts")

        case "4":
            nombre = input("Que equipo desea eliminar? ")

            if(nombre in equipos):
                del equipos[nombre]
                print("Se ha eliminado al equipo ingresado")
            else:
                print("El equipo ingresado no existe")
        case "5":
            print("Finalizacion del programa....")
            break
        
        case _:
            print("Opcion Invalida")
        