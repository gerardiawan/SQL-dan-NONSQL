import pymongo

print("       Program Operasi Management MongoDB ")
print("       Dirgantoro Gerardiawan (19/447114/SV/16833)            ")
print("=====================================================\n")
print("Menu Management User via MongoDB")
print("1. Create database dan tabel")
print("2. Insert data")
print("3. Select/search data")
print("4. Update data")
print("5. Delete data")
menu=input("Silahkan pilih operasi ( 1/2/3/4/5 ) ? ")
print("Anda memilih : " + menu)

if menu=='1' :
    print("Create database dan tabel")
    # create a database
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["managementuserdb"]
    print(client.list_database_names())
    
    # create a collection
    col = db ["managementuser"]
    print(db.list_collection_names())

    #create a content or insert
    mylist = [
        { "_id": 1, "name": "Siska", "pass": "qwerty", "stat": "tersedia"},
        { "_id": 2, "name": "Nami", "pass": "orange", "stat": "tersedia"}
        ]
    x = col.insert_many(mylist)
    #print list of the _id values of the inserted documents:
    print(x.inserted_ids)
    for x in col.find():
        print(x)

elif menu=='2' :
    print("Insert data")
    #insert
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["managementuserdb"]
    col = db ["managementuser"]
    mylist = { "_id": 3, "name": "Zoro", "pass": "onepiece", "stat": "tersedia" }
    x = col.insert_one(mylist)
    print(x.inserted_id)
    
    mydict = { "_id": 4, "name": "Luffy", "pass": "Nakama", "stat": "tersedia" }

    x = col.insert_one(mydict)

elif menu=='3' :
    print("Select/search data")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["managementuserdb"]
    col = db ["managementuser"]
    #search data
    myquery = { "name": "Zoro" }
    mydoc = col.find(myquery)
    for x in mydoc:
        print(x)

elif menu=='4' :
    print("Update data")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["managementuserdb"]
    col = db ["managementuser"]
    #update data
    myquery = { "name": "Zoro" }
    newvalues = { "$set": { "name": "Sanji" } }
    col.update_one(myquery, newvalues)
    #print "customers" after the update:
    for x in col.find():
        print(x)

elif menu=='5' :
    print("Delete data")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["managementuserdb"]
    col = db ["managementuser"]
    #delete data
    myquery = { "pass": "onepiece" }
    col.delete_one(myquery)