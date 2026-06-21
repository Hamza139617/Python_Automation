import requests
from bs4 import BeautifulSoup
import csv
import sys

## lists for storing the data
titles = []
prices = []
ratings = []
availability = []
dataItem = []

file = open("newfile.csv", "a", encoding="utf-8", newline="")

for page in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    try:
        response = requests.get(url)
    except requests.ReadTimeout as rt :
        print("ReadTimeout occured " + rt)
        sys.exit(1)
    

    soup = BeautifulSoup(response.text, "html.parser")



    for anchor in soup.find_all("h3"):
        for child in anchor:
            titles.append(child.get("title").strip())             

    ## now for price

    for price in soup.find_all(class_="price_color"):
        prices.append(price.get_text()[2:].strip()) # did it because there is no specific sign for pound


    for rating in soup.find_all(class_="product_pod"):
        rates = rating.find("p")
        ratings.append(rates.get("class")[1].strip())

    for availabilit in soup.find_all(class_="instock availability"):
        availability.append(availabilit.get_text().strip())
    
    

    writer = csv.writer(file)
    
    for index in range(len(titles)):
        dataItem.append(titles[index])
        dataItem.append(prices[index])
        dataItem.append(ratings[index])
        dataItem.append(availability[index])

        writer.writerow(dataItem)
        dataItem.clear()
    
    

    titles.clear()
    ratings.clear()
    prices.clear()
    availability.clear()


file.close()