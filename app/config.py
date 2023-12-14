# config.py

class Config:
    # Debug mode
    DEBUG = True

    # Database configuration
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@db/home_automation'
    SQLALCHEMY_TRACK_MODIFICATIONS = False