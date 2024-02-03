from selenium.webdriver.common.by import By

def model_products(products, identifiers) -> list:
    def model_product(product) -> dict:
        product_price = product.find_element(By.CSS_SELECTOR, f"span.{identifiers["price"]}").text
        product_img = product.find_element(By.CSS_SELECTOR, f"img.{identifiers["img"]}").get_attribute("src")
        product_name = product.find_element(By.CSS_SELECTOR, f"span.{identifiers["name"]}").text
        product_amount = product.find_element(By.CSS_SELECTOR, f"p.{identifiers["amount"]}").text

        return {"name": product_name, "img": product_img, "price": product_price, "amount": product_amount}

    
    return list(map(model_product,products))

