import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()
url = 'https://jumpbooks.lk/bestselling-books-in-sri-lanka/'
response = scraper.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.text)
