'''
**** Wsgi server file
'''
import os
import unittest

# from flask.cli import FlaskGroup
from apps.main.config import Config, Environment
from apps.main import create_app
from apps import blueprint

config = Config(Environment(os.getenv("FLASK_ENV", "development")))

app = create_app(config)
app.register_blueprint(blueprint)

app.app_context().push()

# cli = FlaskGroup(app)

# @cli.command
# def run():
    # app.run(host='0.0.0.0',port=5001)

# @cli.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('tests/')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    # cli()
<<<<<<< HEAD
=======
    # test()
>>>>>>> feature_branch
    app.run(host='0.0.0.0',port=5001)
