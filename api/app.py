# coding: utf-8
"""
url shortener app
"""
import logging
import os

from flask import Flask
from api import sys, url


def create_app(test_config=None):
    """
    create an app instance
    :param test_config:
    :return:
    """
    # create and configure the app
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        application.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        application.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    logging.basicConfig(level=logging.DEBUG)
    # apply the blueprints to the app
    app.register_blueprint(sys.bp)
    app.register_blueprint(url.bp)

    return application


app = create_app()
