import requests 
from bs4 import BeautifulSoup 
import csv

URL = "https://biopharmguy.com/links/state-ma-all-geo.php"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html5lib') 
print(soup.prettify()) 
companyurl=[]  # a list to store company urls
  
table = soup.find('div', attrs = {'id':'siteContainer'}) 
for row in table.findAll('div', attrs = {'class':'table'}): 
    quote = {} 
    
    quote['url'] = row.a['href'] 
    quote['company'] = row.p.text 
    quotes.append(quote) 
  
filename = 'test.csv'
with open(filename, 'wb') as f: 
    w = csv.DictWriter(f,['url','company']) 
    w.writeheader() 
    for quote in quotes: 
        w.writerow(quote) 
