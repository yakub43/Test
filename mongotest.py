import pymongo

client = pymongo.MongoClient("mongodb+srv://james43:james123@cluster0.1vlp1xz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "james",
    "email" : "james@123",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)