import os
from environs import Env

basedir = os.path.abspath(os.path.dirname(__file__))

env = Env()
env.read_env(".env", recurse=False)


class Config:
    DEBUG = env.bool("DEBUG", default=False)
    SECRET_KEY = env.str("SECRET_KEY", default="SecretKey")


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URL = env.str("DATABASE_URL", default="postgres://root:3210@127.0.0.1:5432/expense_tracker")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URL = env.str("DATABASE_URL", default="postgres://root:3210@127.0.0.1:5432/expense_tracker")
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URL = env.str("DATABASE_URL")


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
