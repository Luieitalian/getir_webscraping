from utils import get_products
from utils import write_to_json
from selenium import webdriver

et_balik_url = "https://getir.com/buyuk/kategori/et-tavuk-balik-P1593VdPBd/"
identifiers = {"article": "ccXlDA",
               "name": "jFvYQy", "img": "hDQjIU", "price": "jmELbE", "amount": "dmgfcc"}

driver = webdriver.Firefox()
write_to_json("et_balik/et_balik", get_products(et_balik_url, identifiers, driver))
driver.quit()
