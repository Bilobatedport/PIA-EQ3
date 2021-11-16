from os import remove
import re
import requests
from bs4 import BeautifulSoup as bs



# nombre = input("Nombre: ")

def redSocial(doc):
    resp = input("Desea agregar una red social? (s/n): ")
    while True:
        if resp == 's':
            RedSocialDict = dict()
            nombreRS = input("Red social: ")
            perfilRS = input("Perfil: ")
            RedSocialDict[nombreRS] = perfilRS
            for elem2 in RedSocialDict:
                doc.write(elem2 + " : " + RedSocialDict[elem2] + '\n')
            print("Red social agregada exitosamente!")
            resp = input("Desea agregar otra red social?(s/n): ")

        elif resp == 'n':
            break
        else:
            resp = input("Favor de ingresar una opcion valida")


def extractPersonalData(name):
        newName = re.sub(r' ','_',name)
        nacionalidad = re.compile(r"^[A-Za-z]")
        regexNacimiento = re.compile(r'\d{1,2}\sde\s\w{4,10}\sde\s\d{4}')
        try:
            wiki = requests.get(f"https://es.wikipedia.org/wiki/{newName}")
            sp = bs(wiki.content, "html.parser")
            with open("temp.txt", "w", encoding="utf-8")as f:
                for data in sp.findAll("div", class_="mw-body"):
                    for tabledata in data.findAll(class_="infobox biography vcard"):
                        for tr in tabledata.findAll("tr"):
                            for td in tr.findAll("td"):
                                f.write(td.text)
            with open("temp.txt", "r+", encoding="utf-8")as fr:
                fr.readline()
                fr.seek(0)
                with open("DatosAux.txt", "w", encoding="utf-8")as doc:
                    for linea in fr.readlines():
                        if regexNacimiento.match(linea):
                            new = re.sub(r'\(\d*\saños\)', '\n', linea)

                            doc.write(new)
            remove("temp.txt")
            dicData = dict()
            with open("DatosAux.txt", "r+", encoding="utf-8")as doc2:

                listaData = list()
                doc2.readline()
                doc2.seek(0)
                for line in doc2.readlines():
                    listaData.append(line)
                dicData["Nacimiento"] = listaData[0]
                dicData["Nacionalidad"] = listaData[1]
            remove("DatosAux.txt")
            with open("DatosPersonales.txt", "w", encoding="utf-8")as doc3:
                for elem in dicData:
                    doc3.write("\n" + elem + " : " + dicData[elem] + "\n")
                redSocial(doc3)

        except:
            print(f"El algoritmo no es capaz de encontrar información de {name}")



# extractSocialMedia("Cillian-Murphy")


