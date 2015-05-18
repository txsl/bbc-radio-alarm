from datetime import date
from subprocess import call

import requests
from bs4 import BeautifulSoup



# Get the pid of the programme

schedule_url = date.today().strftime("http://www.bbc.co.uk/radio4/programmes/schedules/%Y/%m/%d")

print schedule_url

r = requests.get(schedule_url)

soup = BeautifulSoup(r.text)

morning_sec = soup.find(id='morning')

programmes = morning_sec.findAll("div", {"class": "programme__body"})

for p in programmes:

    # print p.find("span", {"class": "programme__title"}).text
    # print "Today" in p.find("span", {"class": "programme__title"}).text

    if "Today" in p.find("span", {"class": "programme__title"}).text:
        # pid = p.find("span", {"class": "programme__title"}).span['resource'].split('/')[-1]
        pid = p.a['href'].split("/")[-1]
        print "Found Today. PID = %s" % pid


# Download the programme

call(["get_iplayer", "--type=radio", "--get", "--aactomp3", "--pid=%s" % pid])