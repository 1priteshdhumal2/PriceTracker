import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

url = 'https://www.amazon.in/MuscleBlaze-Protein-Glutamic-Mango-Servings/dp/B08RNYNGM6/ref=sr_1_3_sspa?keywords=whey+protein&qid=1676353110&sprefix=whey%2Caps%2C270&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'

try:
    response = requests.get("https://proxy.scrapeops.io/v1/", 
                            params={
                              'api_key': '547dec94-1b9c-44f5-9196-6d3ae41e456d',
                              'url': url
                            },
                            headers=headers)
    
    if response.status_code != 200:
        print(f"The request was not successful. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")

#Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find the product price
product_price = soup.find('span',{'class':'a-price-whole'})
if product_price:
    product_price = product_price.text.strip().replace(",","")
    print(f"Product Price: {product_price}")
else:
    print("Product Price not found")
