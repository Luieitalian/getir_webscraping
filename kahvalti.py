from utils import get_products
from utils import write_to_json
from utils import save_images
from selenium import webdriver

category = "kahvalti"
url = "https://getir.com/buyuk/kategori/kahvalti-iat0l1yrkf/"
identifiers = {"article": "ccXlDA",
               "name": "jFvYQy", "img": "hDQjIU", "price": "jmELbE", "amount": "dmgfcc"}

driver = webdriver.Firefox()
write_to_json(category, get_products(url, identifiers, driver))
save_images(category)
driver.quit()
