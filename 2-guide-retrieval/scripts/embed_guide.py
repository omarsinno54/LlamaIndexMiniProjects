import sys
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, root_dir)


from utils.constants import OPEN_AI_API_KEY
from openai import OpenAI

os.environ['OPENAI_API_KEY'] = OPEN_AI_API_KEY
client = OpenAI()

def get_embedding(text, model='text-embedding-3-small'):
    text = text.replace('\n', ' ')

    return client.embeddings.create(
        input = [text],
        model = model
    ).data[0].embedding