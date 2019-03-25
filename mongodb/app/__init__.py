#!/usr/bin/env python
# coding=utf-8

from flask import Flask

from app.database import DB
from app.models.job import Job


def create_app(config):
    app = Flask(__name__)
    DB.init()
    register_blueprints(app)
    for job_name in ['job1', 'job2', 'job3']:
        new_job = Job(name=job_name)
        new_job.insert()
    return app


def register_blueprints(app):

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
