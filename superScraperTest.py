from bs4 import BeautifulSoup
from superScraper import SuperScraper

# Initialize the scraper
scraper = SuperScraper()


url = 'https://jumpbooks.lk/bestselling-books-in-sri-lanka/'

try:
    html = scraper.get(url)

 
    soup = BeautifulSoup(html, 'html.parser')

    print("Page Title:", soup.title.text)
    
    bestsellers = soup.find_all('h2')  
    print("Bestsellers:")
    for book in bestsellers:
        print("-", book.text.strip())
except Exception as e:
   
    print("Error:", e)
