from flask import render_template, url_for, flash, redirect
from blogapp import app
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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') #success is a bootstarap class
        return redirect('home')
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data=='password':
            flash('You have been logged in!', 'success')
            return redirect('home')
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title="Login", form=form)
