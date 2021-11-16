import re
import argparse

import EscaneoDePuertos.EscaneosDePuertos
from WebScrapping import WebScrappingProgram
from EscaneoDePuertos import EscaneosDePuertos



#print("-----------------------------------------\n"
 #     "          Hacking Tool for PC \n"
  #    "-----------------------------------------")

#Menu
#print("(1) Web Scrapping\n"
 #     "(2) Escaneo de puertos\n"
  #    "(3) Cifrado de mensajes\n"
   #   "(4) Envío de correos\n"
    #  "(5) Keylogger\n")

#patron = re.compile(r'[1-5]')

#opcion = input("Opcion: ")

#ArgParse
parser = argparse.ArgumentParser(description='Hacking Tool')
parser.add_argument('-wS',metavar='nombre', type=str, help='   Persona a buscar')
args = parser.parse_args()
nombre = args.wS
WebScrappingProgram.mainWS(nombre)








# while True:
#       if patron.match(opcion):
#             # WebScrapping
#             if opcion == 1:
#                   WebScrapping.mainWS()
#                   break
#
#             #Escaneo de puertos
#             elif opcion == 2:
#                   EscaneosDePuertos.ShootYourShot()
#                   break
#
#             #Cifrado de mensajes
#             elif opcion == 3:
#                   continue
#             elif opcion == 4:
#                   continue
#             elif opcion == 5:
#                   continue
#             break
#       else:
#             opcion = input("Escribir una opción valida: ")






