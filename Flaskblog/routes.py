from flask import render_template,url_for,flash,redirect
from Flaskblog import app
from Flaskblog.forms import  RegistrationForm,LoginForm
from Flaskblog.models import User,Post

posts = [
    {
        'author': 'Phillip Tyler',
        'title':'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 21,2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 20,2019'
    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.userName.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #fake data for successful login
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in ', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful, please check username and password', 'danger')
    return render_template('login.html',title='Login',form=form)
