import logging
import sys
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, root_dir)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from utils.constants import OPENAI_API_KEY

from llama_index.core import (
        VectorStoreIndex, 
        SimpleDirectoryReader,
        StorageContext,
        load_index_from_storage
    )

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

persist_dir = os.path.join(root_dir, 'storage')
log_dir = os.path.join(root_dir, 'logs')
data_dir = os.path.join(root_dir, 'data')

# Load the data
has_storage = bool(os.listdir(persist_dir)) # If list is empty, does not have storage
if has_storage:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)
else:
    # does not exist, retrieve information from documents
    documents = SimpleDirectoryReader(data_dir).load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=persist_dir)

# Query the LLM
query_engine = index.as_query_engine()
response = query_engine.query('What did the author do growing up?')

print(response)