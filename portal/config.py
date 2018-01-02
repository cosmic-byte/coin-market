import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'i\xd1w\xd0\x84q\x18\\\xd0\xf3\x84\x12\xf1\xb4\xe6\xd2\xbf\x0fc=gl\xcf\x8a'
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'portal.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'portal.db')


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod= ProductionConfig
)
