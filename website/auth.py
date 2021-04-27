from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

#website routes/pages
@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>You are logged out. </p>"

@auth.route('/sign_up')
def signUp():
    return render_template("sign_up.html")