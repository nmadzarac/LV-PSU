#Na stranici http://iszz.azo.hr/iskzl/exc.htm moguće je dohvatiti podatke o kvaliteti zraka za Republiku Hrvatsku. Podaci
#se mogu preuzeti korištenjem RESTfull servisa u XML ili JSON obliku. Koristite skriptu AirQualityRH.py koja
#dohvaća podatke te ih pohranjuje u odgovarajući DataFrame. Prepravite/nadopunite skriptu s programskim kodom
#kako bi dobili sljedeće rezultate:
#1. Dohvaćanje mjerenja dnevne koncentracije lebdećih čestica PM10 za 2017. godinu za grad Osijek.
#2. Ispis tri datuma u godini kada je koncentracija PM10 bila najveća. 

import urllib.request
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def fetch_air_quality_data():
    url = 'http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=0&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017'
    data = urllib.request.urlopen(url).read()
    return ET.fromstring(data)

def process_data(root):
    rows = []
    for i, child in enumerate(root):
        mjerenje = float(child.find('mjerenje').text)
        vrijeme = child.find('vrijeme').text
        rows.append({'mjerenje': mjerenje, 'vrijeme': vrijeme})
    df = pd.DataFrame(rows)
    df['vrijeme'] = pd.to_datetime(df['vrijeme'], utc=True)
    df['month'] = df['vrijeme'].dt.month
    df['dayOfweek'] = df['vrijeme'].dt.dayofweek
    return df

def plot_data(df):
    df.plot(x='vrijeme', y='mjerenje')
    plt.show()

def get_top_3_days(df):
    return df.nlargest(3, 'mjerenje')

if __name__ == "__main__":
    root = fetch_air_quality_data()
    df = process_data(root)
    plot_data(df)
    print("Top 3 dana s najvećom koncentracijom PM10:")
    print(get_top_3_days(df))
