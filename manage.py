import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.portal import create_app, db

app = create_app(os.getenv('PORTAL_ENV') or 'dev')
manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
