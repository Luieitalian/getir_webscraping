from selenium.webdriver.common.by import By

def model_product(product):
    def model_productt():
        pass

    model_productt()
    product_name = product.find_element(By.CSS_SELECTOR, "span.gXitDI").text
    product_img = product.find_element(By.TAG_NAME, "img").get_attribute("src")
    product_price = product.find_element(By.CSS_SELECTOR, "span.grTSzD").text
    product_amount = product.find_element(By.CSS_SELECTOR, "p.dmgfcc").text

    return {"name": product_name, "img": product_img, "price": product_price, "amount": product_amount}

