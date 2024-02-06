from utils import get_products
from utils import write_to_json
from utils import save_images
from selenium import webdriver

category = "et_balik"
et_balik_url = "https://getir.com/buyuk/kategori/et-tavuk-balik-P1593VdPBd/"
identifiers = {"article": "ccXlDA",
               "name": "jFvYQy", "img": "hDQjIU", "price": "jmELbE", "amount": "dmgfcc"}

driver = webdriver.Firefox()
write_to_json(category, get_products(et_balik_url, identifiers, driver))
save_images(category)
driver.quit()
