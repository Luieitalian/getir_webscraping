from utils import get_products
from utils import write_to_json
from utils import save_images
from selenium import webdriver

category = "fit_form"
url = "https://getir.com/buyuk/kategori/fit-form-A9ciT987qU/"
identifiers = {"article": "ccXlDA",
               "name": "jFvYQy", "img": "hDQjIU", "price": "jmELbE", "amount": "dmgfcc"}

driver = webdriver.Firefox()
write_to_json(category, get_products(url, identifiers, driver))
save_images(category)
driver.quit()
