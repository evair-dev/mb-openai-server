import os

# Flask
env = os.environ.get('ENV', 'development')
debug = os.environ.get('DEBUG', True)


class Config:
    ENV = env
    DEBUG = bool(debug)

