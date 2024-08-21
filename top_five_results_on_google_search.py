import requests
from bs4 import BeautifulSoup

def scrape_google(query):
    url = f'https://www.google.com/search?q={query}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    for item in soup.find_all('h3', limit=5):
        results.append(item.get_text())
    return results
