# -*- coding: utf-8 -*-
"""Application configuration."""
import os


class Config(object):
    """Base configuration."""

    SECRET_KEY = ' 078906365bc99d2553a367161f5c46e94f5eb5c6'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'production'
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""
    ENV = 'development'
    DEBUG = True
