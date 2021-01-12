import pymongo
import random

myclient = pymongo.MongoClient()
mydb = myclient["shop"]
mystore = mydb["stores"]


# prod = []
# cursor3 = myproducts.find()
# for i in cursor3:
#     prod.append(i)

# categories = {}
# for x in mycat.find():
#     x.pop("_id")
#     categories = x.copy()


class Products:
    def __init__(self):
        self.collection = mydb["products"]

    def get_all(self):
        return list(self.collection.find())

    def get_product_by_cat(self, cat):
        prod = self.collection.aggregate([{"$match": {"category.1": cat}}])
        return list(prod)

    def prod_list(self):
        prodlist = [i for i in self.collection.find({}, {"_id": 0, "name": 1, "category": 1, "price": 1, "brand": 1})]
        return prodlist

    def get_by_id(self, id):
        myquery = {"_id": id}
        proddetails = list(self.collection.find(myquery))[0]
        return proddetails

    def prod_add(self, name, cat, st_id, qu, price, brand, pic_id):
        dic = {"name": name,
               "category": cat,
               "price": [{"store_id": st_id,
                          "quantity": qu,
                          "price": price}],
               "brand": brand,
               "pic_id": pic_id}
        self.collection.insert_one(dic)

    def prod_delete(self, id):
        myquery = {"pic_id": id}
        self.collection.delete_one(myquery)

    def by_cat(self, cat):
        query1 = {"category": cat}
        x = self.collection.find(query1)
        l = []
        for i in x:
            l.append(i)
        return l

    def quantity_list(self):
        pipeline = [{"$unwind": "$price"},
                    {"$project": {"_id": 0}},
                    {"$group": {"_id": "$name", "quantity": {"$sum": "$price.quantity"}}}]
        return (count for count in self.collection.aggregate(pipeline))


class Categories:
    def __init__(self):
        self.collection = mydb["categories"]
        self.my_cat = list(self.collection.find({}, {"_id": 0}))[0]

    def get_category(self):
        return self.my_cat.keys()

    def get_sub_category(self, cat):
        return self.my_cat[cat]

    def get_object(self):
        return self.my_cat


class Stores:
    def __init__(self):
        self.collection = mydb["stores"]

    def ware_list(self):
        return (warehouse for warehouse in self.collection.find({}, {"name": 1}))

    def ware_add(self, dic):
        return self.collection.insert_one(dic)

    def ware_delete(self, name):
        myquery = {"name": name}
        self.collection.delete_one(myquery)

    def ware_quantity(self):
        pipeline = [{"$unwind": "$items"},
        {"$project": {"name": 1, "items.name": 1, "items.quantity": 1,"items.price": 1}}]
        return (count for count in self.collection.aggregate(pipeline))


class Orders:
    def __init__(self):
        self.collection = mydb["orders"]

    def order_add(self, name, items):  # items=[{kala:panir,gheymat:12200,tedad:1},{kala:medad,gheymat:...}
        dic = {"نام و نام خانوادگی": name,
               "کالاها": items
               }
        self.collection.insert_one(dic)


# cursor = mystore.find({}, {"items": 1, "_id": 0})

# goods_of_store1_item = cursor[0]
# goods_of_store1 = goods_of_store1_item["items"]
# goods_of_store1 = random.choices(goods_of_store1, k=35)
# print(goods_of_store1[0])
# goods_of_store1 = []
# for product in prod:
#     goods_of_store1.append(product)


def get_db():
    db = {
        'amir': "mohseni",
        'id': 1234
    }
    return db
