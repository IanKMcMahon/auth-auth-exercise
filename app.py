from flask import Flask, render_template, redirect, session, flash
from models import connect_db, db, User
# from forms import RegisterForm, LoginForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///auth-auth"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "ihaveasecret"
app.app_context.push()

connect_db(app)
db.create_all()


app = Flask(__name__)


@app.route('/')
def show_homepage():
    """redirect to register page when not logged in"""

    return redirect('/register')

@app.route('/register')
def show_user_form():
    """ Show a form that when submitted will register/create a user """


@app.route('/register', methods=["POST"])
def submit_user_form():
    """Handle new user form submission, redirect to /secret"""



# **GET */ :*** Redirect to /register.

# **GET */register :*** Show a form that when submitted will register/create a user. This form should accept a username, password, email, first_name, and last_name. Make sure you are using WTForms and that your password input hides the characters that the user is typing!

# **POST */register :*** Process the registration form by adding a new user. Then redirect to ***/secret***

# **GET */login :*** Show a form that when submitted will login a user. This form should accept a username and a password. Make sure you are using WTForms and that your password input hides the characters that the user is typing!

# **POST */login :*** Process the login form, ensuring the user is authenticated and going to ***/secret*** if so.

# **GET */secret :*** Return the text “You made it!” (don’t worry, we’ll get rid of this soon)