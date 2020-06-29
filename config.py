import os

class Config(object):
    """Config file"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-very-strong-secret-key'


