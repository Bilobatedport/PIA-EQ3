from bs4 import BeautifulSoup as bs
import requests
from os import remove
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def titulares(name):
    google = "https://www.google.com"
    results = int(input("Numero News: "))
    page = requests.get(
        google + f"/search?q={name}&rlz=1C1CHBF_esMX892MX892&sxsrf=ALeKk02F9HHkoEDOVDHCWkbQdJZRo660lQ:1621818951897&source=lnms&tbm=nws&sa=X&ved=2ahUKEwis2ZG0kuHwAhVNZK0KHZSrCCwQ_AUoAnoECAEQBA&num={results}")
    soup = bs(page.content, "html.parser")
    html = soup.findAll("a")

    listaAux = list()
    listaLinks = list()
    titulos = list()
    str1 = ""

    for link in html:
        link_href = link.get("href")
        if "/url?q=" in link_href:
            listaAux.append(link_href)

    listaAux.pop()
    listaAux.pop()
    listaLinks.append("https://asldkjalsdj")
    for link in listaAux:
        new = link.replace("/url?q=", "")
        listaLinks.append(new)
    for link in  listaLinks:
        try:
            query = requests.get(link)
            if query.status_code == 200:
                pass
            else:
                listaLinks.remove(link)
        except:
            listaLinks.remove(link)
    with open("tempNoticias.txt", "w", encoding="utf-8")as document:
        for link in listaLinks:
            document.write(link + '\n')

    with open("tempNoticias.txt", "r", encoding="utf-8")as documentRead:
        documentRead.readline()
        documentRead.seek(0)
        for linea in documentRead.readlines():
            page = requests.get(linea)
            soup = bs(page.content, "html.parser")
            for h1 in soup.findAll("h1"):
                titulos.append(h1.text)
    remove("tempNoticias.txt")
    titulos = list(set(titulos))
    for elem in titulos:
        str1 = str1 + elem + "\n"
    with open("Titulares.txt","w", encoding="utf-8") as titulares:
        titulares.write(str1)
