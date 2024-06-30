import chromadb
import sys
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, root_dir)

data_dir = os.path.join(root_dir, 'data')


client = chromadb.PersistentClient(path = data_dir)

def set_collection(documents: list):
    collection = client.create_collection(
        name = 'shogun-guide'
    )

    ids = list(range(len(documents)))

    response = collection.add(
        documents = documents,
        ids = ids
    )
    
    return collection

def get_collection():
    print('--> getting collection')
    return client.get_collection(
        name = 'shogun-guide'
    )