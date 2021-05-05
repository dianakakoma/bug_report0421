from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . models import Report
from . import db

views = Blueprint('views', __name__)

#home page - you cannot get here unless you are logged in
@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        report = request.form.get('report')
        req = request.form
        title = req.get('title')
        issue = req.get('issue')
        url = req.get('url')

        if len(title) < 2:
            flash('The issue description is too short!', category='error')
        else:
            new_report = Report(title=title, issue=issue, url=url, user_id=current_user.id)
            db.session.add(new_report)
            db.session.commit()
            flash('Report added!', category='success')
    return render_template('home.html', user= current_user)