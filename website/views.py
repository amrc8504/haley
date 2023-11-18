from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html', user=current_user)

@views.route('/Profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@views.route('/Account', methods=['GET', 'POST'])
@login_required
def account():
    return render_template('acct_details.html', user=current_user)

@views.route('/ContactUs', methods=['GET', 'POST'])
@login_required
def contact():
    return render_template('contact.html', user=current_user)

@views.route('/Congratulations', methods=['GET', 'POST'])
@login_required
def flowers():
    return render_template('flowers.html', user=current_user)

@views.route('/From-Anthony', methods=['GET', 'POST'])
@login_required
def message():
    return render_template('message.html', user=current_user)