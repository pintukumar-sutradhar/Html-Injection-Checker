# crawler.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

def crawl(url, max_depth=3):
    """Crawl the website to discover forms and parameters with deep crawling."""
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    visited = set()
    forms = []
    params = set()

    def crawl_page(url, depth):
        if depth > max_depth or url in visited:
            return
        visited.add(url)
        try:
            response = requests.get(url)
            if response.status_code != 200:
                return
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract forms
            for form in soup.find_all('form'):
                action = form.get('action', '')
                method = form.get('method', 'get')
                inputs = [(input.get('name', ''), input.get('type', 'text')) for input in form.find_all('input')]
                forms.append({'action': urljoin(base_url, action), 'method': method, 'inputs': inputs})

            # Extract parameters from GET requests
            query_params = re.findall(r'[\?&](\w+)=', response.url)
            params.update(query_params)

            # Extract and follow links
            for link in soup.find_all('a', href=True):
                link_url = urljoin(base_url, link.get('href'))
                if urlparse(link_url).netloc == parsed_url.netloc:
                    crawl_page(link_url, depth + 1)
        
        except requests.RequestException as e:
            print(f"Request failed: {e}")

    crawl_page(url, 0)
    return {'forms': forms, 'params': list(params)}
