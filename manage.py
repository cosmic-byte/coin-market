import os
from portal import create_app, db

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from portal.models import user, course

app = create_app(os.getenv('PORTAL_ENV') or 'dev')
manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
