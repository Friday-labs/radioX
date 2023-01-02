'''
**** Wsgi server file
'''
import os
import unittest

from flask.cli import FlaskGroup
from apps.main.config import config_dict
from apps.main import create_app
from apps import blueprint

get_config_mode = os.getenv('BOILERPLATE_ENV') or 'Dev'
try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
app.register_blueprint(blueprint)

app.app_context().push()

# cli = FlaskGroup(app)

# @cli.command
# def run():
    # app.run(host='0.0.0.0',port=5001)

# @cli.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    # cli()
    app.run(host='0.0.0.0',port=5001)