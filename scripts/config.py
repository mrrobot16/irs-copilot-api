import os
from os.path import join, dirname
from dotenv import load_dotenv
import base64

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

with open('./credentials/firebase/.pem', 'rb') as file:
    key_content = file.read()
    encoded_key = base64.b64encode(key_content).decode('utf-8')

decoded_key = base64.b64decode(encoded_key).decode('utf-8')
print(len(decoded_key))
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
print(len(PRIVATE_KEY))
