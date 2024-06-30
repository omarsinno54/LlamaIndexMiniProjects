from db_guide import set_collection, get_collection
from llm_guide import load_documents, query_engine
from scrape_guide import scrape_website
# from tokenize_guide import normalize_data, remove_stopwords_from_data
# from embed_guide import get_embedding

import logging
import sys
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, root_dir)

data_dir = os.path.join(root_dir, 'data')

from utils.loggers import logger

import argparse

class GuideRetrieval:
    def __init__(self):
        self.titles_list = []
        self.text_list = []
        self.embeddings = []

    def retrieve_data(self, url):
        guide_titles, guide_descriptions = scrape_website(url)

        for i, (tit, des) in enumerate(zip(guide_titles, guide_descriptions)):
            document_dir = os.path.join(data_dir, f'{tit}.txt')

            if not os.path.isfile(document_dir):

                with open(document_dir, 'w') as document_file:
                    document_file.write(des)

        self.text_list = guide_descriptions
        self.titles_lsit = guide_titles
    
    def chunk_data(self):
        pass
    
    def clean_data(self):
        cleaned_text_list = []

        for text in self.text_list:
            _clean_text = normalize_data(text)

            cleaned_text_list.append(_clean_text)
        
        self.text_list = cleaned_text_list

    def embed_data(self):
        for text in self.text_list:
            embed_text = get_embedding(text)
            self.embeddings.append(embed_text)
        
        logger.info(f'[i] There are {len(self.embeddings)} embeddings.')

    def vector_db_data(self):
        return set_collection(self.text_list)
    
    def query_data(self, query: str):
        index = load_documents()

        response = query_engine(index, query)

        return response

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', required=True)

    args = parser.parse_args()
    query = args.query

    guide_retrieval = GuideRetrieval()

    url = 'https://steamcommunity.com/sharedfiles/filedetails/?id=2206372652'

    guide_retrieval.retrieve_data(url)
    response = guide_retrieval.query_data(query)

    logger.info(response)
    # guide_retrieval.clean_data()

    # guide_retrieval.embed_data()
    # collection = guide_retrieval.vector_db_data()

    # logger.info(collection.peek())
    # logger.info(collection.count())