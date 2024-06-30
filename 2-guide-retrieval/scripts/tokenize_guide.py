import nltk.corpus
import re
nltk.download('stopwords')

from nltk.corpus import stopwords
stop = stopwords.words('english')

def normalize_data(text: str) -> str:
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text

def stem_data(text: str) -> str:
    pass

def remove_stopwords_from_data(text: str) -> str:
    return ' '.join([word for word in text.split(' ') if word in stop])