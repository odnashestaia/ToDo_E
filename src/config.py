import os
from dotenv import load_dotenv

load_dotenv()


DB_HOST = os.environ.get('DB_HOST')
DB_PASS = os.environ.get('DB_PASS')
DB_USER = os.environ.get('DB_USER')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')

SECRET_AUTH = os.environ.get('SECRET_AUTH')

REDIS_HOST = os.environ.get('REDIS_HOST')
