from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import model_product

driver = webdriver.Firefox()
driver.get("https://getir.com/buyuk/kategori/meyve-sebze-VN2A9ap5Fm/")

products = driver.find_elements(By.CLASS_NAME, "ccXlDA")
driver.implicitly_wait(15)

products_object_list = list(map(model_product, products))
driver.quit()