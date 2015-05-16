from datetime import date

import requests
from bs4 import BeautifulSoup



# Get the pid of the programme

schedule_url = date.today().strftime("http://www.bbc.co.uk/radio4/programmes/schedules/%Y/%m/%d")

r = requests.get(schedule_url)

soup = BeautifulSoup(r.text)

morning_sec = soup.find(id='morning')

programmes = morning_sec.findAll("div", {"class": "programme__body"})

for p in programmes:
    if p.find("span", {"class": "programme__title"}).text == " Today ":
        pid = p.find("span", {"class": "programme__title"}).span['resource']



# Download the programme