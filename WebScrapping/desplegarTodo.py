import os

def desplegar_Archivo_Directorios(Directorio = ""):
    listaStuff = os.listdir(os.getcwd() + "\\\\" + Directorio)
    listaDirectorios = list()
    listaArchivos = list()

    for item in listaStuff:
        if os.path.isdir(os.getcwd() + "/" + Directorio + "/" + item):
            listaDirectorios.append(item)
        else:
            listaArchivos.append(item)

    cantidadDirectorios = len(listaDirectorios)
    cantidadArchivos = len(listaArchivos)

    contAux = 1  # Para poder conocer el número del archivo u directorio
    if cantidadDirectorios > cantidadArchivos:
        print("Directorios:\t\t\t\t\t\t\t\t\tArchivos:\n")
        contadorArchivos = 0  # Aumentar el recorrido de archivos

        for directorio in listaDirectorios:
            try:
                print(f"{contAux}.- {directorio}\t\t\t\t\t\t\t\t\t")
                contAux += 1
            except:
                print("\t\t\t\t\t\t\t\t\t")
                pass
            try:
                print(f"\t\t\t\t\t\t\t\t\t{contAux}.- {listaArchivos[contadorArchivos]}\n")
                contAux += 1
            except:
                print("\n")
                pass
            contadorArchivos += 1
    elif cantidadDirectorios < cantidadArchivos:
        print("Archivos:\t\t\t\t\t\t\t\t\tDirectorios:\n")
        contadorDirectorios = 0

        for archivo in listaArchivos:
            try:
                print(f"{contAux}.- {archivo}\t\t\t\t\t\t\t\t\t\t\t")
                contAux += 1
            except:
                print(f"\t\t\t\t\t\t\t\t\t\t\t{contAux}.-")
                pass
            try:
                print(f"\t\t\t\t\t\t\t\t\t\t\t{contAux}.- " + listaDirectorios[contadorDirectorios] + "\n")
                contAux += 1
            except:
                print("\n")
                pass
            contadorDirectorios += 1
    else:
        print("Directorios:\t\t\t\t\t\t\t\t\t\t\tArchivos:\n")
        contadorArchivos = 0  # Aumentar el recorrido de archivos
        for directorio in listaDirectorios:
            print(f"\t{contAux}.- " + directorio + f"\t\t\t\t\t\t\t\t\t\t\t{contAux}.- " +
                  listaArchivos[contadorArchivos] + "\n")
            # print("\t" + directorio + f" : ({contAux})\t\t\t\t\t\t\t\t\t\t\t" + listaArchivos[
            #     contadorArchivos] + f" : ({contAux + 1})\n")
            # contAux += 1
            contadorArchivos += 1
    return listaStuff
