from et_balik import products_object_list as et_balik_prods
#from su_icecek import products_object_list as su_icecek_prods
from meyve_sebze import products_object_list as meyve_sebze_prods
import json

all_products = meyve_sebze_prods 

with open("sample.json" ,"w") as out:
    out.write("[")
    for prod_obj in all_products:
        json_object = json.dumps(prod_obj, indent=4)
        out.write(json_object)
        out.write(",")
    out.write("]")
