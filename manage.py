import operator
import os
import unittest
import coverage

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.portal.api import blueprint as api_blueprint

from app.portal import create_app, db, socketio
from app.portal.frontend import frontend
from app.portal.models import user, blacklist, message


basedir = os.path.abspath(os.path.dirname(__file__))
app = create_app(os.getenv('PORTAL_ENV') or 'dev')

app.register_blueprint(frontend)
app.register_blueprint(api_blueprint)
app.app_context().push()

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


@manager.command
def routes():
    'Display registered routes'
    rules = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        rules.append((rule.endpoint, methods, str(rule)))

    sort_by_rule = operator.itemgetter(2)
    for endpoint, methods, rule in sorted(rules, key=sort_by_rule):
        route = '{:50s} {:25s} {}'.format(endpoint, methods, rule)
        print(route)

if __name__ == '__main__':
    manager.run()