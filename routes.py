from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from . import app, db
from .models import User, Project
from .forms import LoginForm

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        if user:
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)

@app.route('/Aboutus')
def about():
    return render_template('Aboutus.html')

@app.route('/Contactus')
def contact():
    return render_template('Contactus.html')
