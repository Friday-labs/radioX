#######################################
"""
****** 
Configuration for environment [Debug, Production, Test] and Mongodb url

******
""" 
#######################################
import os
class Config(object):

    # Set up the App SECRET_KEY
    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_007')
    DEBUG = False
    ###Mongodb Config
    MONGO_KEY = "fridayRadioX"#os.environ['MONGO_KEY']
    MONGO_URI =  "mongodb+srv://FridayInc:"+MONGO_KEY+"@radioxcluster0.rvpjb8i.mongodb.net/radiox?retryWrites=true&w=majority"
    MONGODB_DB_NAME = 'radiox'

class ProductionConfig(Config):
    DEBUG = False


class DebugConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Dev'     : DebugConfig,
    'Test' : TestingConfig
}


