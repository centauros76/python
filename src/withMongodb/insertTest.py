import pymongo


def db_conn():
    conn = pymongo.MongoClient('127.0.0.1', 27017)
    return conn

conn = db_conn()
db = conn.get_database('python_test')
collection = db.get_collection('memo_test')

#for i in range(1, 101) :
#    id = collection.insert_one({'number':i, 'memo':'hello python %d' % i}).inserted_id
#    print(id)



filter = {'number':{'&gt':20}}
count_filter = collection.count_documents(filter)
print(count_filter)

#count_all = collection.estimated_document_count()
#print(count_all)

total = collection.find({})
for aa in total:
    print(aa)

conn.close()

