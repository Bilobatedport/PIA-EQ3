import sys
import requests
import urllib.parse
import urllib.request
import os, time, random
from bs4                import BeautifulSoup as bs
from progress.bar       import ChargingBar  # install progress

import WebScrapping.rotacion_Proxies
from WebScrapping.edicion     import agregar,editar,eliminar
from WebScrapping.rotacion_Proxies  import download_image
from WebScrapping.personalData       import extractPersonalData
from WebScrapping.desplegarTodo      import desplegar_Archivo_Directorios
from WebScrapping.Articulos          import titulares
from WebScrapping.API                import situacionClimatologica
from WebScrapping.archivosExcel      import documentExcel

def descargarImagen(nombre,results):
    os.mkdir("Imagenes")
    os.chdir("Imagenes")
    page = requests.get(f"https://www.google.com/search?q={nombre}&tbm=isch&ved+-twitter.com+-youtube.com&num={results}")
    soup = bs(page.content, "html.parser")
    numeroImagen = 0
    for img in soup.findAll("img"):
        link = img.get("src")
        download_image(link, os.getcwd(),f"Imagen_{nombre}x{str(numeroImagen)}")
        numeroImagen += 1

def busquedaTitulares(link):
    page = requests.get(link)
    soup = bs(page.content, "lxml")

    for h1 in soup.findAll("h1"):
        return h1

    pass

def mainWS(nombre):
    WebScrapping.rotacion_Proxies.Inizialicacion()
    WebScrapping.rotacion_Proxies.main(sys.argv)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    actualPath = os.getcwd()
    carpetaLista = os.listdir(actualPath)
    #nombre = input("Ingresar nombre de deportista o famoso: ") #INGRESAR NOMBRE
    nombreCarpeta = nombre + '/'
    nombreArchivo = nombre + 'Links.txt'
    nombreArchivoExcel = nombre + 'Links'
    if not nombre in carpetaLista:


        os.mkdir(nombre)
        os.chdir(nombre)
        filedir = r".txt"
        listArcivos = [_ for _ in os.listdir(actualPath) if _.endswith(filedir)]  # TODO Esto crea una lista de archivos txt
        #Verificación de la existencia del TXT
        if not nombreArchivo in listArcivos:
            respuesta1 = input("Ingresar URL's de forma\n"
                               "\t(a)Manual\n"
                               "\t(b)Algoritmo\nAccion: ")
            if respuesta1 == 'a':
                cantidadUrl = int(input("Ingresar la cantidad de URL's a ingresar: "))
                while True:
                    if cantidadUrl > 1:
                        with open(nombreArchivo, "w", encoding='utf-8') as documento:
                            for i in range(cantidadUrl):
                                url = input("URL: ")
                                documento.write(url + '\n')
                        print("Las URL's se han guardado exitosamente\n\nDescargando Imágenes...\n")
                        #TODO descargar imagenes

                        break
                    elif cantidadUrl == 1:
                        with open(nombreArchivo, "w", encoding='utf-8') as documento:
                            url = input("URL: ")
                            documento.write(url)
                        print("La URL se ha guardado exitosamente\n\nDesscargando Imágenes...\n")
                        #TODO descargar imagenes
                        #shutil.move(nombreArchivo, nombreCarpeta)
                        break

                    else:
                        cantidadUrl = int(input("Favor de ingresar una cantidad valida: "))



            elif respuesta1 == 'b':
                results = int(input("Ingresar número de links a buscar y agregar en el archivo TXT: "))
                page = requests.get(f"https://www.google.com/search?q={nombre}+-twitter.com+-youtube.com&num={results}",
                                    headers=headers)
                soup = bs(page.content, "html.parser")
                htmlList = soup.findAll("a")
                ligasLista = list()
                barLinks = ChargingBar('\bRecolectando ligas:', max=results) #+-youtube.com

                with open(nombreArchivo, 'w', encoding='utf-8') as document:
                    for link in htmlList:
                        link_href = link.get('href')
                        if "url?q=" in link_href and not "webcache" in link_href:
                            liga = link.get('href').split("?q=")[1].split("&sa=U")[0]
                            new_liga = liga.replace('%3F', '?')
                            new_liga2 = new_liga.replace('%3D', '=')
                            new_liga3 = urllib.parse.unquote(new_liga2)
                            new_liga4 = urllib.parse.unquote(new_liga3)
                            ligasLista.append(new_liga4)
                            time.sleep(random.uniform(0, 0.2))
                            barLinks.next()

                    for i in range(2):
                        ligasLista.pop()
                    for liga in ligasLista:
                        document.write(liga + '\n')
                    barLinks.finish()
                    print(f"El algoritmo ha recolectado {results} ligas de manera satisfactoria.")
            print("Recolectando datos personales...\n")
            extractPersonalData(nombre)
            print("Datos personales recolectados satisfactoriamente!\n")
            print("Recolectando articulos de noticias...\n")
            titulares(nombre)
            print("Articulos recolectados!\n")
            print("Generando el archivo excel...\n")
            documentExcel(nombreArchivoExcel, "Titulares", "DatosPersonales")
            print("El archivo excel ha sido generado exitosamente!\n")
            cantidadImg = int(input("Numero de imagenes a descargar:"))
            print("\nDescargando Imágenes...\n")
            descargarImagen(nombre, cantidadImg)
            print("Las imagenes han sido descargadas satisfactoriamente!\n")

            situacionClimatologica()




        else:
            print("Ya hay un archivo de texto con ligas existente, ¿desea editarlo o eliminarlo?: \n"
                  "\t(1) Eliminar\n"
                  "\t(2) Editar\n"
                  "\t(3) Regresar al menú principal\n"
                  "\t(4) Salir")
            respuesta = input("Acción:")
            while True:
                if respuesta == '1':
                    os.remove(nombreArchivo)
                    input("Presione enter para finalizar el programa")
                    break
                elif respuesta == '2':
                    with open(nombreArchivo, 'w') as documento:
                        lineas = int(input("Cuántas URL's escribirá?"))
                        for i in range(lineas):
                            url = input("URL: ")
                            documento.write(url+ '\n')
                        print("Las URL's ingresadas han sido guardadas exitosamente.")


                    input("Presione enter para finalizar el programa")
                    break
                elif respuesta == '3':
                    os.system('cls')
                    mainWS(nombre)
                elif respuesta == '4':
                    sys.exit()
                else:
                    respuesta = input("Favor ingresar una respuesta valida: ")
    else:
        print("Ya se ha hecho un WebScraping a " + nombre + ".")
        while True:

            print("Qué desea proceder a hacer:\n"
                  "\t (a) Desplegar su contenido\n"
                  "\t (b) Eliminar la carpeta con toda la investigacion previa\n"
                  "\t (c) Salir")

            resp = input("Acción: ")
            #TODO Desplegar contenido
            if resp == 'a':
                os.system("cls")
                #TODO inicio de la función
                desplegar_Archivo_Directorios(nombre)
                #TODO Fin de la función

                # print("Directorios:\t\t\t\t\t")
                # for directorio in listaDirectorios:
                #     print("\t" + directorio)
                eleccion = input("Escribir el nombre del listado mostrado: ")
                while True:
                    if eleccion in os.listdir(os.getcwd()+"/" + nombre):
                        # Menú anterior
                        while True:
                            print("\n\n"
                                  "Qué desea proceder a hacer: \n"
                                  "\t (a) Editar su contenido\n"
                                  "\t (b) Volver al menú anterior\n"
                                  "\t (c) Salir")
                            respuesta = input("Acción: ")
                            if respuesta == 'a':
                                if eleccion.endswith(".txt"):
                                    while True:
                                        os.system("cls")
                                        print("Que desea hacer?:\n"
                                              "\t(a)Agregar  linea\n"
                                              "\t(b)Editar   linea\n"
                                              "\t(c)Eliminar linea\n"
                                              "\t(d)Salir")
                                        decision = input()
                                        while True:
                                            os.system("cls")
                                            if decision == 'a':  # Agregar linea
                                                agregar(nombreCarpeta,eleccion)
                                                break

                                            elif decision == 'b':  # Editar linea
                                                editar(nombreCarpeta,eleccion)
                                                break

                                            elif decision == 'c':  # Eliminar
                                                eliminar(nombreCarpeta,eleccion)
                                                break

                                            elif decision == 'd':
                                                sys.exit()
                                            else:
                                                decision = input("Ingresar una opcion valida: ")
                                else:
                                    try:
                                        desplegar_Archivo_Directorios(eleccion)
                                    except:
                                        print("Lo que ha elegido no es archivo y tampoco directorio")
                                        sys.exit()
                            if respuesta == 'b':
                                break
                    else:
                        eleccion = input("Favor de ingresar una eleccion válida: ")
            elif resp == 'b':
                dirPath = os.getcwd()+"/" + nombre

                try:
                    os.rmdir(dirPath)
                except OSError as e:
                    print(f"Error:{e.strerror}")
                break
            elif resp == 'c':
                exit()




