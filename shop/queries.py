import pymongo
myclient=pymongo.MongoClient()
mydb=myclient["shop"]
coll_products=mydb["products"]
coll_store=mydb["stores"]
##------------------------------------prod_list
def prod_list():
    prodlist=[i for i in coll_products.find({},{ "_id": 0, "name": 1, "category": 1,"price":1, "brand":1 })]
    return prodlist
##------------------------------------prod_details
def prod_details(id):
    myquery = { "pic_id": id }
    proddetails=[i for i in coll_products.find(myquery)]
    return proddetails
##------------------------------------prod_add
def prod_add(name,cat,st_id,qu,price,brand,pic_id):
    dic={"name":name,
         "category":cat,
         "price":[{"store_id":st_id,
                   "quantity":qu,
                   "price":price}],
         "brand" :brand,
         "pic_id": pic_id}
    coll_products.insert_one(dic)
##------------------------------------prod_edit


##------------------------------------prod_delete
def prod_delete(id):
    myquery = {"pic_id": id}
    coll_products.delete_one(myquery)
##------------------------------------prod_upload


##------------------------------------ware_list
def ware_list():
    return [i for i in coll_store.find({},{"_id":0,"name":1})]
##------------------------------------ware_add
def ware_add(dic):
    coll_store.insert_one(dic)
##------------------------------------ware_edit
def ware_edit(name):
    pass
##------------------------------------ware_delete
def ware_delete(name):
    myquery={"name":name}
    coll_store.delete_one(myquery)
##------------------------------------quantity_list
def quantity_list():
    pipeline = [{"$unwind": "$price"},
                {"$project" : { "_id" : 0 } },
                {"$group": {"_id":"$name","quantity":{"$sum":"$price.quantity"}}}]
    return [i for i in coll_products.aggregate(pipeline)]
for i in quantity_list():
    print(i)
##------------------------------------quantity_add








cats=[]
y= coll_products.find({},{"_id":0,"category": 1 })
for i in y:
    c=i["category"]
    if not c in cats:
        cats.append(c)



def by_cat(cat):
    query1={"category" : cat}
    x=coll_products.find(query1)
    l=[]
    for i in x :
        l.append(i)
    return l
# print(by_cat(cats[5]))

