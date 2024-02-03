from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import model_products

product_element_identifiers = {"name": "jFvYQy", "img": "hDQjIU", "price": "jmELbE", "amount": "dmgfcc"}

driver = webdriver.Firefox()
driver.get("https://getir.com/buyuk/kategori/su-icecek-ewknEvzsJc/")

products = driver.find_elements(By.CLASS_NAME, "ccXlDA")
driver.implicitly_wait(15)

products_object_list = model_products(products, product_element_identifiers)
driver.quit()