import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from app.portal.config import basedir


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.portal.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/market'
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.portal.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'market.db')
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.portal.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()