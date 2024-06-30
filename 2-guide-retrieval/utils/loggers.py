import logging
import sys
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
data_dir = os.path.join(root_dir, 'logs')

logs_dir = os.path.join(data_dir, 'logs.txt')

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create Stream Handler
s_handler = logging.StreamHandler()
s_handler.setLevel(logging.DEBUG)
logger.addHandler(s_handler)

# Create File Handler
f_handler = logging.FileHandler(logs_dir)
f_handler.setLevel(logging.DEBUG)
logger.addHandler(f_handler)