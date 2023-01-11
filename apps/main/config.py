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

    # MongoDB configuration
    MONGO_KEY = "fridayRadioX" # Add the MongoDB key here
    MONGO_URI =  "mongodb+srv://FridayInc:{MONGO_KEY}@radioxcluster0.rvpjb8i.mongodb.net/radiox?retryWrites=true&w=majority"
    MONGODB_DB_NAME = 'radiox'
    
    def __init__(self, environment: Environment):
        self.environment = environment
        if environment == Environment.PRODUCTION:
            self.DEBUG = False
        elif environment == Environment.DEVELOPMENT:
            self.DEBUG = True
        elif environment == Environment.TESTING:
            self.DEBUG = True
            self.TESTING = True