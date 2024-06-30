from urllib.request import urlopen
from bs4 import BeautifulSoup

import sys
import os


root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, root_dir)

data_dir = os.path.join(root_dir, 'data')
documents_dir = os.path.join(data_dir, 'documents')

from utils.loggers import logger

def scrape_website(url: str, label: str = None) -> list:
    '''
        Helper function used to scrape text
        from a URL.
        :param url: string representing the URL to scrape from.
        :return: response dictionary.
    '''
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode('utf-8')

    subsection_title = '<div class="subSectionTitle">'
    subsection_desc = '<div class="subSectionDesc">'
    subsection_end = '</div>'

    subsection_desc_pattern = f'{subsection_desc}.*?{subsection_end}'
    soup = BeautifulSoup(html, 'html.parser')
    
    subsection_descriptions = soup.find_all('div', class_='subSectionDesc') # < subsection description
    subsection_descriptions = [text.get_text().strip('\n\r\t') for text in list(subsection_descriptions)]

    subsection_titles = soup.find_all('div', class_='subSectionTitle')
    subsection_titles = [title.get_text().strip('\n\r\t') for title in list(subsection_titles)]

    return subsection_titles, subsection_descriptions

if __name__ == '__main__':
    url = 'https://steamcommunity.com/sharedfiles/filedetails/?id=2206372652'
    response = scrape_website(url)