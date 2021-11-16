import datetime
import geocoder
import requests
import json
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=5)
    print(text)

DIRECCION = "Monterrey, México"
loc = geocoder.osm(DIRECCION)
lat = loc.latlng[0]
lon = loc.latlng[1]

def situacionClimatologica():
    # API_KEY = "30efe26788ba96c5698aa05f43c0b6ab"
    headers = {
        'Cache-Control': 'no-cache'
    }

    querystring = {f"lat": lat, "lon": lon, "appid": "30efe26788ba96c5698aa05f43c0b6ab", "units": "metric",
                   "lang": "38"}

    response = requests.request("GET", "https://api.openweathermap.org/data/2.5/weather/", headers=headers,
                                params=querystring)
    data = json.loads(response.content)
    jprint(data)
    hora_UTC = datetime.datetime.fromtimestamp(data['dt'])
    amanecer = datetime.datetime.fromtimestamp(data['sys']["sunrise"])
    atardecer = datetime.datetime.fromtimestamp(data['sys']["sunset"])

    print('')
    print('Condiciones climatologicas')
    print('Latitud:', data['coord']['lat'])
    print('Longitud:', data['coord']['lon'])
    print('Temperatura:', data['main']['temp'])
    print('Sensación termica:', data['main']['feels_like'])
    print('Temperatura minima:', data['main']['temp_min'])
    print('Temperatura máxima:', data['main']['temp_max'])
    print('Presión atmosferica:', data['main']['pressure'])
    print('Humedad:', data['main']['humidity'])
    print('Visibilidad:', data['visibility'])
    print('Velocidad del viento', data['wind']['speed'])
    print('Dirección del viento:', data['wind']['deg'])
    print('Abundancia de nubes:', str(data['clouds']['all']) + ' %')
    print('Hora cálculo datos:', hora_UTC.strftime('%d-%m-%Y %H:%M:%S'))
    print('Código país:', data['sys']['country'])
    print('Hora amanecer:', amanecer.strftime('%H:%M:%S'))
    print('Hora atardecer:', atardecer.strftime('%H:%M:%S'))
    print('Población:', data['name'])
    print('Código población:', data['id'])

# parameters = {
#     "lat": lat,
#     "lon": lon,
#     "dt_txt": "2021-5-27 21:00:00"
# }
# page = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API_KEY}", params=parameters)
# jprint(page.json())


#
# page = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?{lat}&{lon}&lang=es&exclude=current,minutely,hourly,alerts&appid={API_KEY}", params=parameters)
# jprint(page.json())
# page2 = requests.get(f"http://api.scrape.do?token=91ea598c1ce048c09197d8699ed358bb557c24809ef&url=http://httpbin.org/ip?json")
# jprint(page2.json())
#
#
#
# web_scrapper = Web_Scrapper()
# web_scrapper.set_scrape_do_config(api_token="91ea598c1ce048c09197d8699ed358bb557c24809ef")
# resp = web_scrapper.scrape_do(url_to_scrape="https://github.com/narkhedesam/Proxy-List-Scrapper/blob/master/Web_Scrapper/README.md", method="GET", payload={}
#                               ,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}, render=False, super_proxies=False, geo_code=None)
#
# print(resp)
























