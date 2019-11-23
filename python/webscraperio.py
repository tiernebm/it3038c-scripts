import requests, re
from bs4 import BeautifulSoup

r = requests.get("https://colemans.com/product-category/clothing/coats/").content
soup = BeautifulSoup(r, "lxml")
span = soup.findAll("span", {'class' : 'price'})
for span in span:
    print("Price=" + span.text)

