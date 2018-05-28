import requests
from bs4 import BeautifulSoup

url = 'http://www.dytt8.net/'

res = requests.get(url)
if res.status_code == 200:
    soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')
    new_films = soup.select('div[class="co_content8"]')
    for item in new_films[0].find_all("tr"):
        


    