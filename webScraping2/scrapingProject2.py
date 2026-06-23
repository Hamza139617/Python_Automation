from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv




p = sync_playwright().start()

brands = []
names = []
ratings = []
prices = []


browser = p.chromium.launch(headless=False)

for pageNum in range(1, 21):

    page = browser.new_page()

    url = f"https://www.amazon.in/s?k=iphone&crid=V2C54OZMCB4W&qid=1782214826&sprefix=iphon%2Caps%2C468&xpid=7f5t0w2UV8ecn&ref=sr_pg_{pageNum}"

    page.goto(
            url,
            wait_until="load"
        )

    

    html = page.content()
    page.close()


    with open("amazon.html", "w", encoding="utf-8") as f:
        f.write(html)

    soup = BeautifulSoup(html, "html.parser")





    # extracting the brands first 
    #for brand in soup.find_all(class_="a-size-medium a-color-base"):
    #    brands.append(brand.get_text())

    items = soup.select("div[data-component-type='s-search-result']")

    for item in items:
        title_tag = item.find("h2", class_="a-size-medium a-spacing-none a-color-base a-text-normal")
        brand_h2  = item.find("h2", class_="a-size-mini s-line-clamp-1")
        rate = item.find("span", class_="a-size-small a-color-base")
        price = item.find("span", class_="a-price-whole")

        
        if price:
            prices.append(price.get_text())

        else:
            prices.append(" ")

        if title_tag:
            names.append(title_tag.get_text(strip=True))
        else:
            names.append(" ")



        if brand_h2:
            span = brand_h2.find("span", class_="a-size-medium a-color-base")
            brands.append(span.get_text(strip=True) if span else "Ths")
           
        else:
            brands.append(" ")


        if rate:
            ratings.append(rate.get_text())
        else:
            ratings.append(" ")



with open("items.csv", "w", encoding="utf-8") as file:

    dataItem = []
    writer = csv.writer(file)

    for item in range(len(names)):
        dataItem.append(names[item])
        dataItem.append(ratings[item])
        dataItem.append(brands[item])
        dataItem.append(prices[item])

        writer.writerow(dataItem)
        dataItem.clear()





browser.close()
p.stop()

