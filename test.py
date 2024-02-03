from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import model_products

product_element_identifiers = {"name": "jFvYQy", "img": "hDQjIU", "price": "jmELbE", "amount": "dmgfcc"}

driver = webdriver.Firefox()
driver.get("https://getir.com/buyuk/kategori/su-icecek-ewknEvzsJc/")

driver.implicitly_wait(15)
els = driver.find_elements(By.CSS_SELECTOR, "p.dmgfcc")

for el in els:
  print(el.text)
  