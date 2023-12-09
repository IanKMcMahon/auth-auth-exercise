from flask import Flask, render_template, redirect, session, flash
from models import connect_db, db, User
from forms import RegisterForm
# from forms import RegisterForm, LoginForm

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

form = UserForm()
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
    render_template('login.html')

@app.route('/login', methods=["POST"])
def submit_login_form():
    """Handle login form submission, redirect to /secret"""

@app.route('/secret')
def display_secret_content():
    """secret landing page for once a user is registered/logged in"""

    return "YOU MADE IT!!"

# @app.route('/logout')
# def logout_user():
