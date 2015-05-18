import requests
from bs4 import BeautifulSoup


BASE_URL = "http://www.bbc.co.uk/programmes/"

def bbc_is_available(pid):

    url = BASE_URL + pid

    r = requests.get(url)

    bs = BeautifulSoup(r.text)

    if "after broadcast" in bs.find('div', {'class': 'smp__message'}).text:
        return False
    else:
        return True

