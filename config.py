import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secreto-123')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
