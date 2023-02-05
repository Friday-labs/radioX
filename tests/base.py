from flask_testing import TestCase
from apps.main.config import Config, Environment
from wsgi import app
# from apps.main import create_app
import os


class BaseTestCase(TestCase):
    """ Base Tests """
    config = Config(Environment(os.getenv("FLASK_ENV", "testing")))

    def create_app(self):
        # app = create_app(self.config)
        app.config.from_object(self.config)
        return app