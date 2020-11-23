# coding: utf-8
import pymongo
def get_collection_data(mongo, db_name):
    myclient = pymongo.MongoClient(mongo)
    dblist = myclient.list_database_names()
    db = myclient[db_name]
    collections = db.list_collection_names()
    print(collections)
    data = db.command("collstats",collections[0])
    data_size = data["size"]
    collection_size = {}
    for c in collections:
        c_data = db.command("collstats", c)
        collection_size[c] = int(c_data["size"])
    sort_tables = sorted(collection_size.items(),key=lambda item:item[1],reverse=True)
    return (sort_tables, collection_size)

if __name__ == "__main__":
    mongo = "mongodb://10.88.50.10:27017/"
    (sorted_tables, collection_size) = get_collection_data(mongo,"sweeper")
    g_data = 0.0
    for t in sorted_tables:
        g_data = g_data + t[1]/1073741824.0
    print("total_data size: "+ str(g_data))
    
    select_g_data =  0.0
    # with open("./ben_tables.txt","r") as f:
    #     k = f.readline()
    #     while k:
    #         select_g_data = select_g_data + collection_size[k[0:-1]]/1073741824.0
    #         k = f.readline()
    #         print(k)
    # print(select_g_data)
    




# if __name__ == "__main__":
#     myclient = pymongo.MongoClient("mongodb://10.88.50.10:27017/")
#     dblist = myclient.list_database_names()
#     print(dblist)
#     wishpost = myclient.wishpost
#     collections = wishpost.list_collection_names()
#     print(collections)
#     print(collections[0])
#     print(wishpost.command("collstats",collections[0]))
#     data = wishpost.command("collstats",collections[0])
#     data_size = data["size"]
#     print(data_size)
#     collection_size = {}
#     with open("./raw_data",'w') as f:
#         for c in collections:
#             c_data = wishpost.command("collstats", c)
#             f.writelines(c + "        " + str(c_data["size"]) +"\n") 
#             collection_size[c] = int(c_data["size"])
    
#     sort_tables = sorted(collection_size.items(),key=lambda item:item[1],reverse=True)
#     # with open("./sorted_table_sweeper","w") as f:
#     #     g_data = 0.0
#     #     for t in sort_tables:
#     #         f.write(t[0] + " : " + str(t[1]) + "\n")

    
#     g_data = 0.0
#     with open("./ben_tables.txt","r") as f:
#         k = f.readline()
#         while k:
#             g_data = g_data + collection_size[k[0:-1]]/1073741824.0
#     print(g_data)


    
    