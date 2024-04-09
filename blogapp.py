from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '92edb5d9eb7c2c56718e58dbdd5ab578' 

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


if __name__ == "__main__":
	app.run(debug=True)
