from flask import Flask, render_template, redirect, session, flash
from models import connect_db, db, User
from forms import RegisterForm, LoginForm, FeedbackForm, DeleteForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///auth-auth"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "ihaveasecret"
app.app_context().push()

connect_db(app)
db.create_all()


app = Flask(__name__)


@app.route('/')
def show_homepage():
    """redirect to register page when not logged in"""

    return redirect('/register')

@app.route('/register')
def show_registration_form():
    """ Show a form that when submitted will register/create a user """

form = RegisterForm()

render_template('register.html', form=form)

@app.route('/register', methods=["POST"])
def submit_registration_form():
    """Handle new user form submission, redirect to /secret"""

form = RegisterForm()
if form.validate_on_submit():

    username = form.username.data
    password = form.password.data
    email = form.email.data
    first_name = form.first_name.data
    last_name = form.last_name.data
    new_user = User.register(username, password, email, first_name, last_name)

    db.session.add(new_user)
    db.session.commit()


@app.route('/login')
def show_login_form():
    """Display form for logging in existing user"""
    form = LoginForm()
    
    render_template('login.html', form=form)

@app.route('/login', methods=["POST"])
def submit_login_form():
    """Handle login form submission, redirect to /secret"""
    form = LoginForm()
    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            flash(f"Welcome Back, {user.username}!", "primary")
            session['user_id'] = user.id
            return redirect('/tweets')
        else:
            form.username.errors = ['Invalid username/password.']

    return render_template('login.html', form=form)

def display_secret_content():
    """secret landing page for once a user is registered/logged in"""

    return "YOU MADE IT!!"

# @app.route('/logout')
# def logout_user():
