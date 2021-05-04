from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
#import user security functionality - runs a hashing function on the password
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

#website routes/pages
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #get data entered in the login form
        email = request.form.get('email')
        password = request.form.get('password')

        #return the first result with a matching email address
        user = User.query.filter_by(email=email).first()
        if user:
            #if the user is found, check the hashed password entered in the form against what is already hashed and stored
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash("Email does not exist.", category='error')
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>You are logged out. </p>"

# sign-up form
@auth.route('/sign_up', methods=['GET','POST'])
def signUp():
    #get information entered in the sign-up form
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #search for existing email addresses to make sure that the email address does not already exist.
        user= User.query.filter_by(email=email).first()

        # validating sign-up information & error message flashing
        if user:
            flash("Email already exists.", category='error')
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category='error')
        elif len(firstName) < 2:
            flash("First name must be greater than 1 character.", category='error')
        elif len(password1) < 7:
            flash("Password length must be at least 7 characters.", category='error')
        elif password1 != password2:
            flash("Passwords must match.", category='error')
        else:
            # if no errors have been encountered - create the new based on the database model
            newUser = User(email=email, firstName=firstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(newUser)
            db.session.commit()
            
            flash('Account created!', category="success")

            #after account is successfully created redirect the new user to the homepage.
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")