# -*- coding: utf-8 -*-
"""Application configuration."""
import os


class Config(object):
    """Base configuration."""

    SECRET_KEY = ' 078906365bc99d2553a367161f5c46e94f5eb5c6'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    CACHE_TYPE = 'redis'
    CACHE_KEY_PREFIX = 'flask_cookie_'
    # redis://user:password@localhost:6379/0
    CACHE_REDIS_URL = os.environ.get('CACHE_REDIS_URL')


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'production'
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""
    ENV = 'development'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:@localhost/test?charset=utf8mb4"

    CACHE_REDIS_URL = 'redis://root:@localhost:6379/0'
