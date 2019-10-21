import pymongo

conn = pymongo.MongoClient('127.0.0.1', 27017)
print(conn)

db = conn.get_database('python_test')
print(db)

collection = db.get_collection('memo_test')
print(collection)

collecitonList = db.list_collection_names()
print(collecitonList)

conn.close()
