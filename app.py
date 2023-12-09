from flask import Flask, render_template, redirect, session, flash
from models import connect_db, db, User
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


@app.route('/register', methods=["POST"])
def submit_registration_form():
    """Handle new user form submission, redirect to /secret"""

@app.route('/login')
def show_login_form():
    """Display form for logging in existing user"""

@app.route('/login', methods=["POST"])
def submit_login_form():
    """Handle login form submission, redirect to /secret"""

@app.route('/secret')
def display_secret_content():
    """secret landing page for once a user is registered/logged in"""

    return "YOU MADE IT!!"

# @app.route('/logout')
# def logout_user():
