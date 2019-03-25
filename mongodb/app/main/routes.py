# Copyright 2019 Arie Bregman
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from flask import render_template

from app.main import bp  # noqa
from app.models.job import Job


@bp.route('/')
def index():
    """Main page route."""
    button_text = "Add Job"
    return render_template('main.html', button_text=button_text)


@bp.route('/add_job')
def add_job():
    """Adds job4 to the database."""
    new_job = Job(name='job4')
    new_job.insert()
    return ('', 204)
