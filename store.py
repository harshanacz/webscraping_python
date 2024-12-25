import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()

url = 'https://www.daraz.lk/womens-fashion/?page=1'
response = scraper.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


