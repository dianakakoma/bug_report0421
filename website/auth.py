from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

#website routes/pages
@auth.route('/login', methods=['GET','POST'])
def login():
    #get data entered in the login form
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
    
        # validating sign-up information & error message flashing
        if len(email) < 4:
            flash("Email must be greater than 3 characters.", category='error')
        elif len(firstName) < 2:
            flash("First name must be greater than 1 character.", category='error')
        elif len(password1) < 7:
            flash("Password length must be at least 7 characters.", category='error')
        elif password1 != password2:
            flash("Passwords must match.", category='error')
        #if the inform
        else:
            flash('Account created!', category="success")
    return render_template("sign_up.html")