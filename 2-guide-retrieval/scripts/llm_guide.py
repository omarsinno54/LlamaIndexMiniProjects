from llama_index.core import (
        VectorStoreIndex, 
        SimpleDirectoryReader,
        StorageContext,
        load_index_from_storage
    )

import sys
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, root_dir)

from utils.constants import OPEN_AI_API_KEY
from utils.loggers import logger

os.environ['OPENAI_API_KEY'] = OPEN_AI_API_KEY

persist_dir = os.path.join(root_dir, 'storage')
log_dir = os.path.join(root_dir, 'logs')
data_dir = os.path.join(root_dir, 'data')

# Load the data
def load_documents():
    has_storage = bool(os.listdir(persist_dir)) # If list is empty, does not have storage

    if has_storage:
        # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context)
    else:
        # does not exist, retrieve information from documents
        documents = SimpleDirectoryReader(data_dir).load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=persist_dir)
    
    return index

# Querying the LLM
def query_engine(index, query: str):

    query_engine = index.as_query_engine(streaming=True)
    query_engine.query(query).print_response_stream()

    print('\n')
    return query_engine.query(query)