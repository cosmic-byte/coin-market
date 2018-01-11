import os
import unittest
import coverage

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.portal import create_app, db, socketio
from app.portal.models import user, blacklist


basedir = os.path.abspath(os.path.dirname(__file__))
app = create_app(os.getenv('PORTAL_ENV') or 'dev')

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

COV = coverage.coverage(
    branch=True,
    include='app/*',
    omit=[
        'app/test/*',
        'app/portal/config.py',
        'app/portal/*/__init__.py'
    ]
)
COV.start()


@manager.command
def run():
    socketio.run(app)


@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('app/test')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
