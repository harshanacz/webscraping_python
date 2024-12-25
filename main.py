import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()

processing = True
pageNo = 1

while processing:
    url = "https://www.daraz.lk/womens-fashion/?page=" + str(pageNo)
    response = scraper.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if pageNo > 25:
        processing = False
    else:
        allProducts = soup.find_all("div", class_="Bm3ON")
        for product in allProducts:
            item = {}
            item['Title'] = product.find('img').attrs.get("alt", "No Title")
            print(item["Title"])

    pageNo += 1  
