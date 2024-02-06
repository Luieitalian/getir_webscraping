from utils import get_products
from utils import write_to_json
from utils import save_images
from selenium import webdriver

category = "meyve_sebze"
url = "https://getir.com/buyuk/kategori/meyve-sebze-VN2A9ap5Fm/"
identifiers = {"article": "ccXlDA",
               "name": "jFvYQy", "img": "hDQjIU", "price": "jmELbE", "amount": "dmgfcc"}

driver = webdriver.Firefox()
write_to_json(category, get_products(url, identifiers, driver))
save_images(category)
driver.quit()
