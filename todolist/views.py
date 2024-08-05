
from flask import render_template, redirect, flash, url_for
from flask import session as login_session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from wtforms.validators import DataRequired, Length, Email, EqualTo
from todolist import app, db
from todolist.models import Users, Tasks


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password') ])
    email = StringField('Email', validators=[DataRequired(), Email() ])
    submit = SubmitField("Sign up")


    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email() ])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Login")

class TaskForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    submit = SubmitField("Add")

@app.route("/")
def hello_world():
    message = "Welcome! Would you like to begin?"
    return render_template('index.html', message=message)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(id=form.username.data, email=form.email.data)
        user.setPassword(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and user.checkPassword(form.password.data):
            login_session['username'] = user.id
            return redirect(url_for('listpage'))
        else:
            flash("Incorrect email or password!", 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/listpage', methods=['GET', 'POST'])
def listpage():
    form = TaskForm()
        
    username = login_session['username']
    if form.validate_on_submit():
        tasks = Tasks(task = form.task.data)
        db.session.add(tasks)
        db.session.commit()
    
    try:
        task = Tasks.query.all()
        return render_template('listpage.html', username=username, form = form, task= task)
    except Exception as e:
        error = '<h1>Something is broken</h1>'
        return error


