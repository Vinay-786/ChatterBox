from flask import render_template, request, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from blogapp import app, db, bcrypt
from blogapp.forms import RegistrationForm, LoginForm
from blogapp.models import User, Post


posts = [
 {
  'author': 'Vinay Kumar',
  'title': 'Blog 1',
  'content': 'Hey there, first tweet',
  'date_posted': 'Feb 2, 2024'
 },
 {
  'author': 'Ankit Choudhary',
  'title': 'Blog 2',
  'content': 'Hey there, second tweet',
  'date_posted': 'Feb 3, 2024'
 }
]


@app.route("/")
@app.route("/home")
def hello_world():
	return render_template('home.html', posts=posts)


@app.route("/about")
def about():
	return render_template('about.html', title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('hello_world'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email = form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You can login now.', 'success') #success is a bootstarap class
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('hello_world'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('hello_world'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('hello_world'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
