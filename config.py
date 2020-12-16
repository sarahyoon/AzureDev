import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'hello-world321.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'helloworld-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'qwer123$'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'helloworld765'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'a1yeZj6Cyt55jwC3ATz9J4Z04rR1TssBaStlnlxy6irJk+7Y4a18PzgkFnAfTZSklnRYnl56uejbW0Y1gECe7w=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
