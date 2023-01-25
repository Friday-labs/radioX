import os
from enum import Enum
from dotenv import load_dotenv
from datetime import datetime,timedelta

class Environment(Enum):
    PRODUCTION = "production"
    DEVELOPMENT = "development"
    TESTING = "testing"

class Config(object):
    """
    Configuration for environment [Development, Production, Testing] and MongoDB url
    """
    load_dotenv()
    # Set up the App SECRET_KEY
    # SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_007')
    DEBUG = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1, seconds=5)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=10,seconds=5)
    # MongoDB configuration
    MONGO_URI = os.environ.get('MONGO_URI')
    # Redis Configuration
    #fakeredis.FakeStrictRedis(server=server) for testing
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
    ##Password is not set
    REDIS_URL = 'redis://localhost:6379/0'
    
    def __init__(self, environment: Environment):
        self.environment = environment
        if environment == Environment.PRODUCTION:
            self.DEBUG = False
        elif environment == Environment.DEVELOPMENT:
            self.DEBUG = True
        elif environment == Environment.TESTING:
            self.DEBUG = True
            self.TESTING = True
            self.MONGO_URI = os.getenv('TEST_MONGO_URI')