import json

categories = ["dondurma", "et_balik", "ev_yasam", "firindan", "fit_form",
              "kahvalti", "meyve_sebze", "su_icecek", "sut_urunleri", "teknoloji"]
id_count = 1
all_products = []

def alter_amount_field(obj):
    if obj["amount"] == "":
        obj["amount"] = 1
    obj["amount/attribute"] = obj["amount"]
    obj.pop("amount")

def trim_img(obj):
    obj["img"] = obj["img"].split("/")[4].split("?")[0]

def add_category(obj, category):
    obj["category"] = category

def add_id(obj):
    global id_count
    obj["id"] = id_count
    id_count += 1

def organise(category):
    with open(f"{category}/{category}.json", 'r') as read:
        json_obj_list = json.load(read)
        for obj in json_obj_list:
            add_id(obj)
            alter_amount_field(obj)
            trim_img(obj)
            add_category(obj, category)
        all_products.extend(json_obj_list)

def main():
    for category in categories:
        organise(category)
    with open("all_products.json", 'w') as out:
        writable_all_products = json.dumps(all_products, indent=4)
        out.write(writable_all_products)


if __name__ == '__main__':
    main()
