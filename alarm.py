from datetime import date
from subprocess import call
from time import sleep

import requests
from bs4 import BeautifulSoup

from utilities import bbc_is_available

today = date.today()

# Get the pid of the programme
today = date.today()

schedule_url = today.strftime("http://www.bbc.co.uk/radio4/programmes/schedules/%Y/%m/%d")

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

pid = 'b05v7tnb'

# Check if we can download the file

while True:

    if bbc_is_available(pid):
        break
    else:
        sleep(120)


# Download the programme

date_substring = today.strftime("%d_%m_%Y")

file_name = "today_%s_%s" % (date_substring, pid)

call(["get_iplayer", "--type=radio", "--get", "--pid=%s" % pid, "--file-prefix=%s" % file_name])


