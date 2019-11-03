import requests 
from bs4 import BeautifulSoup 
import csv
URL = "https://biopharmguy.com/links/state-al-all-geo.php"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
for link in soup.find_all(onclick=True):
    print(link.get_text())
    print(link.get('href'))    



