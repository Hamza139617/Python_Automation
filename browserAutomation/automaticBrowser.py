from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={"width":1280, "height":720},
        locale="en-US"
    )

    page = context.new_page()

    page.goto("https://www.saucedemo.com/", wait_until="load")

    # page.locator("#password").fill("secret_sauce")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#user-name").fill("standard_user")
    # page.locator("#login-button").click()

    page.get_by_text("Login").click()

    page.locator(".product_sort_container").select_option(value="za")

    product = page.locator(".inventory_item").filter(has_text="Sauce Labs Onesie")

    product.locator("button").click()

    product2 = page.locator(".inventory_item").filter(has_text="Sauce Labs Fleece Jacket")

    product2.locator("button").click()

    page.locator(".shopping_cart_link").click()

    page.locator("#checkout").click()

    page.locator("#first-name").fill("Hamza")

    page.locator("#last-name").fill("Khan")

    page.locator("#postal-code").fill("19200")

    page.locator("#continue").click()


    soup = BeautifulSoup(page.content(), "html.parser")

    file = open("shippingInfo.txt", "w")

    print(soup.find_all(attrs={"data-test":"payment-info-value"})[0].get_text())
    print(soup.find_all(attrs={"data-test":"shipping-info-value"})[0].get_text())
    print(soup.find_all(attrs={"data-test":"total-label"})[0].get_text())

    file.write("Id " + soup.find_all(attrs={"data-test":"payment-info-value"})[0].get_text() + "\n")
    file.write("Delievery " + soup.find_all(attrs={"data-test":"shipping-info-value"})[0].get_text() + "\n")
    file.write(soup.find_all(attrs={"data-test":"total-label"})[0].get_text())

    page.screenshot(path="details.png")


    page.locator("#finish").click()

    input("please enter ")



    context.close()
    browser.close()