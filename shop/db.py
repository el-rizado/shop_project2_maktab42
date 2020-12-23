import pymongo
import random

myclient = pymongo.MongoClient()
mydb = myclient["shop"]
mycat = mydb["categories"]

categories = {}

for x in mycat.find():
    x.pop("_id")
    categories = x.copy()


mystore = mydb["stores"]

cursor = mystore.find({}, {"items": 1, "_id": 0})

# cursor1 = mystore.aggregate([
#                     {'$unwind': '$items'},
#                     {'$match': {"items.category": "دیجیتال.موبایل"}},
#                     {'$group': {'_id': "items.name", 'mymin': {'$min': "$items.price"}}}
# ])
# for i in cursor:
#     print(i)
goods_of_store1_item = cursor[0]
goods_of_store1 = goods_of_store1_item["items"]
goods_of_store1 = random.choices(goods_of_store1, k=35)

# set_of_categories = set()
# for item in goods_of_store1:
#     set_of_categories.add(item["category"])

# for i in set_of_categories:
#    for item in goods_of_store1:
#        if item["category"] == i:
#            print(item)
#            break




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

