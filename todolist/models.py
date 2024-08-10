from todolist import app
from todolist import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

migrate = Migrate(app, db)

class Users(db.Model, UserMixin):
    id = db.Column(db.String(120), primary_key = True)
    email = db.Column(db.String(120), db.ForeignKey('tasks.task'), nullable=False, index=True, unique = True)
    password_hash = db.Column(db.String(128))
    def setPassword(self, password):
        self.password_hash = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password_hash, password)


class Tasks(db.Model):
    __tablename__ = 'tasks'  # Explicitly defining table name

    task = db.Column(db.Text, primary_key=True)
    task_save = db.relationship('Users', backref='tasks', lazy=True)
