from bs4 import BeautifulSoup
from superScraper import SuperScraper

# Initialize the scraper
scraper = SuperScraper()

# Test URL (change this as needed)
url = 'https://jumpbooks.lk/bestselling-books-in-sri-lanka/'

try:
    # Get the page HTML using SuperScraper
    html = scraper.get(url)

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Print the actual page title (after bypassing Cloudflare)
    print("Page Title:", soup.title.text)
    
    # Assuming bestselling books are inside <h2> tags, print them
    bestsellers = soup.find_all('h2')  
    print("Bestsellers:")
    for book in bestsellers:
        print("-", book.text.strip())
except Exception as e:
    # Print error if something goes wrong
    print("Error:", e)
