from flask import Blueprint, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models import User
from app.extensions import db

bp = Blueprint('auth', __name__)

@bp.route('/login')
def login():
    flash('Steam OpenID authentication endpoint reached.', 'info')
    return redirect(url_for('index'))

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('index'))
