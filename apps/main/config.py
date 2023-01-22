import os
from enum import Enum

class Environment(Enum):
    PRODUCTION = "production"
    DEVELOPMENT = "development"
    TESTING = "testing"

class Config(object):
    """
    Configuration for environment [Development, Production, Testing] and MongoDB url
    """
    # Set up the App SECRET_KEY
    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_007')
    DEBUG = False
    JWT_ACCESS_TOKEN_EXPIRES = None
    # MongoDB configuration
    MONGO_URI =  "mongodb+srv://FridayInc:fridayRadioX@radioxcluster0.rvpjb8i.mongodb.net/radiox?retryWrites=true&w=majority"

    # Redis Configuration
    #fakeredis.FakeStrictRedis(server=server) for testing
    redis_host = "localhost"
    redis_port = 6379
    redis_password = ""
    ##Password is not set
    REDIS_URL = "redis://:password@localhost:6379/0"
    
    def __init__(self, environment: Environment):
        self.environment = environment
        if environment == Environment.PRODUCTION:
            self.DEBUG = False
        elif environment == Environment.DEVELOPMENT:
            self.DEBUG = True
        elif environment == Environment.TESTING:
            self.DEBUG = True
            self.TESTING = True
            self.MONGO_URI = "mongodb+srv://FridayInc:fridayRadioX@radioxcluster0.rvpjb8i.mongodb.net/tests?retryWrites=true&w=majority"