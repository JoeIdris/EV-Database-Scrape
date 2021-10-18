#! G:\anaconda3\python.exe

from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import lxml
import time

def visit_link(url):
    result = requests.get(url)

    if result.status_code != 200:
        print('[!] FAILED TO LOAD WEBSITE: Response status code {}'.format(result.status_code))
        exit(1)

    return BeautifulSoup(result.content, 'lxml')


def scrape_website():
    website = r'https://ev-database.org'
    soup = visit_link(website)

    vehicle_dict = {}
    for idx, vehicle in enumerate(soup.findAll('div', {'class': 'list-item'}), 1)
        make, model = [x.text for x in vehicle.find('a', {'class': 'title'}).findAll('span', {'class': [re.compile(r'[a-z]+'), 'model']})]
        vehicle_name = make + ' ' + model
        battery = vehicle.find('span', {'class': 'battery'}).text
        acceleration, topspeed, range, efficiency, fastcharge = [x.findAll('span')[-1].text for x in vehicle.findAll('p', {'class': 'left'})]


        vehicle_dict[vehicle_name] = vehicle_dict.get(vehicle_name, {})
        keys = ['Battery', 'Acceleration', 'Top Speed', 'Range', 'Efficiency', 'Fast Charge']
        for i in keys:
            vehicle_dict[vehicle_name][i] =

        vehicle_dict[vehicle_name] = vehicle_dict.get(vehicle_name, {})
        vehicle_dict[vehicle_name]['Battery'] = battery
        vehicle_dict[vehicle_name]['Acceleration'] = acceleration
        vehicle_dict[vehicle_name]['Top Speed'] = topspeed
        vehicle_dict[vehicle_name]['Range'] = range
        vehicle_dict[vehicle_name]['Efficiency'] = efficiency
        vehicle_dict[vehicle_name]['Fast Charge'] = fastcharge


        df = pd.DataFrame.from_dict(vehicle_dict, orient='index')

        df.to_csv('ScrapedData.csv')


if __name__ == '__main__':
    scrape_website()
