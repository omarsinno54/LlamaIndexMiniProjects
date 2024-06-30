import sys
import os

import configparser

root_dir = os.path.dirname(os.path.dirname(__file__))
conf_dir = os.path.join(root_dir, 'config/config.conf')

sys.path.insert(0, root_dir)

parser = configparser.ConfigParser()
parser.read(conf_dir)

OPENAI_API_KEY = parser.get(section='api-keys', option='OPENAI_API_KEY')