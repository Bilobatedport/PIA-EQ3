def agregar(nombreCarpeta, eleccion):
    with open(nombreCarpeta + eleccion, "w",
              encoding='utf-8')as documentoEscribir:
        numeroUrl = int(input("Cuantas url agregará?"))
        while True:
            if numeroUrl == 1:
                url = input("URL: ")
                documentoEscribir.write(url + '\n')
                print("URL agregada exitosamente!")
                break
            elif numeroUrl > 1:
                for i in range(numeroUrl):
                    url = input("URL: ")
                    documentoEscribir.write(url + '\n')

                print("URL's agregadas exitosamente!")
                break
            else:
                numeroUrl = int(
                    input("Favor de insertar una opcion valida"))

def editar(nombreCarpeta, eleccion):
    lineasLista = list()
    with open(nombreCarpeta + eleccion, "r")as documentoLeer:
        documentoLeer.readline()
        documentoLeer.seek(0)
        contadorLinea = 0
        for line in documentoLeer.readlines():
            print(contadorLinea + 1, ".- ", line)
            newLine = line.replace('\n', '')
            lineasLista.append(newLine)
            contadorLinea += 1
    numeroLinea = int(input("Escoja el número de linea: "))
    nuevaUrl = input("Ingresar nueva URL: ")
    lineasLista[numeroLinea - 1] = nuevaUrl
    with open(nombreCarpeta + eleccion, "w",
              encoding='utf-8')as documentoEscribir:
        for linea in lineasLista:
            documentoEscribir.write(linea + '\n')
            # print(linea)

        print("La linea ha sido editada satisfactoriamente!")

def eliminar(nombreCarpeta, eleccion):
    lineasLista = list()
    with open(nombreCarpeta + eleccion, "r")as documentoLeer:
        documentoLeer.readline()
        documentoLeer.seek(0)
        contadorLinea = 0
        for line in documentoLeer.readlines():
            print(contadorLinea + 1,".- ", line)
            newLine = line.replace('\n', '')
            lineasLista.append(newLine)
            contadorLinea += 1
    numeroLinea = int(input("Escoja el número de linea: "))
    lineasLista.pop(numeroLinea - 1)
    with open(nombreCarpeta + eleccion, "w")as documentoEscribir:
        for linea in lineasLista:
            documentoEscribir.write(linea + '\n')
            # print(linea)
        print("Se ha eliminado satisfactoriamente la linea!")
