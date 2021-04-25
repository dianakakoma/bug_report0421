from flask import Blueprint

auth = Blueprint('auth', __name__)

#website routes/pages
@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>You are logged out. </p>"

@auth.route('/sign-up')
def signUp():
    return "Signed Up"