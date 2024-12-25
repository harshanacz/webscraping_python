import cloudscraper
from fake_useragent import UserAgent

class SuperScraper:
    def __init__(self):
        # Using fake user-agent for more variability
        self.ua = UserAgent()
        # Create a scraper instance for handling Cloudflare
        self.scraper = cloudscraper.create_scraper()

    def get(self, url):
        # Headers with a random user-agent
        headers = {'User-Agent': self.ua.random}
        try:
            # Use cloudscraper to handle Cloudflare protection
            response = self.scraper.get(url, headers=headers)
            # In case of failure, retry or raise an error
            if "Cloudflare" in response.text or response.status_code in [403, 503]:
                raise Exception(f"Cloudflare blocked the request for {url}")
        except Exception as e:
            raise Exception(f"Failed to fetch {url}: {e}")
        return response.text
