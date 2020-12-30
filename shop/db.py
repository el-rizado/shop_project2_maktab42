import pymongo
import random

myclient = pymongo.MongoClient()
mydb = myclient["shop"]

mycat = mydb["categories"]
mystore = mydb["stores"]
myproducts = mydb["products"]


prod = []
cursor3 = myproducts.find()
for i in cursor3:
    prod.append(i)


categories = {}

for x in mycat.find():
    x.pop("_id")
    categories = x.copy()




cursor = mystore.find({}, {"items": 1, "_id": 0})

# goods_of_store1_item = cursor[0]
# goods_of_store1 = goods_of_store1_item["items"]
# goods_of_store1 = random.choices(goods_of_store1, k=35)
# print(goods_of_store1[0])
goods_of_store1 = []
for product in prod:
    goods_of_store1.append(product)

def get_db():
    db = {
        'amir': "mohseni",
        'id': 1234
    }
    return db


p_list = [
    [1, 'دسته بندی1', 'نام کالا1', 'تصویر1'], [2, 'دسته بندی2', 'نام کالا2', 'تصویر2'],
    [3, 'دسته بندی3', 'نام کالا3', 'تصویر3'], [4, 'دسته بندی4', 'نام کالا4', 'تصویر4']
]

s_list = [
    [1, 'شاپ۱'], [2, 'شاپ2'], [3, 'شاپ3'], [4, 'شاپ4']
]

