# webapp/config.py
import os

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'db')
    MYSQL_USER = os.getenv('MYSQL_USER', 'flaskuser')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'flaskpass')
    MYSQL_DB = os.getenv('MYSQL_DB', 'myflaskapp')

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
