from selenium.webdriver.common.by import By
import json


def model_products(products, ids: dict) -> list:
    def model_product(product) -> dict:
        product_price = product.find_element(
            By.CSS_SELECTOR, f"span.{ids["price"]}").text
        product_img = product.find_element(
            By.CSS_SELECTOR, f"img.{ids["img"]}").get_attribute("src")
        product_name = product.find_element(
            By.CSS_SELECTOR, f"span.{ids["name"]}").text
        product_amount = product.find_element(
            By.CSS_SELECTOR, f"p.{ids["amount"]}").text

        return {"name": product_name, "img": product_img, "price": product_price, "amount": product_amount}

    return list(map(model_product, products))


def get_products(url: str, ids: dict, driver) -> list:
    driver.get(url)
    products = driver.find_elements(By.CLASS_NAME, ids["article"])

    return model_products(
        products, ids)


def write_to_json(name: str, prods: list) -> None:
    with open(f"{name}.json", "w") as out:
        out.write("[")
        for prod_obj in prods:
            json_object = json.dumps(prod_obj, indent=4)
            out.write(json_object)
            out.write(",")
        out.write("]")
        out.seek(out.tell() - 2, 0)
        out.write(" ")