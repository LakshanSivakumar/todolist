from flask import render_template, redirect, flash, url_for
from flask import session as login_session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from wtforms.validators import DataRequired, Length, Email, EqualTo
from todolist import app, db
from todolist.models import Users, Tasks

tasks_query = db.Tasks.query()

for i in tasks_query.tasks:
    print(i)