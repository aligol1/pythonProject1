import requests
from bs4 import BeautifulSoup
import csv

HOST = 'https://www.cma-cgm.com/'
URL = 'https://www.cma-cgm.com/ebusiness/tracking'



def get_html(url, params=''):
    r = requests.get(url, params=params)
    return r

def get_contect(html):
    soup = BeautifulSoup(html, 'html.parser')