import requests
import logging
logging.basicConfig(filename='main.log',level='INFO',format='%(asctime)s: %(levelname)s: %(message)s')

url="http://www.ttss.krakow.pl/internetservice/geoserviceDispatcher/services/stopinfo/stops?left=-648000000&bottom=-324000000&right=648000000&top=324000000"
przystanki = requests.get(url)

def findInDatabase(przystanekNazwa):
    
    loop=0
    czyWystapil=False
    nazwa=""
    
    while(czyWystapil==False):
        if loop==1:
            przystanekNazwa=input("Podaj nazwe przystanku:")
            przystanekNazwa=przystanekNazwa.strip()
            przystanekNazwa=przystanekNazwa.lower()
        for x in przystanki.json()["stops"]:
            if x["name"].lower() == przystanekNazwa:
                print('Znaleziono przystanek: '+x["name"])
                logging.warning('  User podal prawidlowa nazwe przystanku')
                nazwa=x["name"]
                numerPrzystanku=x["shortName"]
                czyWystapil=True
                break
        if czyWystapil==False:
            print("Błędna nazwa przystanku")
            logging.warning('  User podal bledna nazwe przystanku')
            loop=1

    return {'a':"http://www.ttss.krakow.pl/#?stop="+numerPrzystanku+"&mode=departure","b":nazwa}
