import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

APP_ENV = os.environ.get('APP_ENV')

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENAI_GPT4_API_KEY = os.getenv("OPENAI_GPT4_API_KEY")

TESTING = True

DEBUG = True