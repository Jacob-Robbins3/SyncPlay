from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
import uuid
from app.models import Lobby, LobbyMember
from app.forms import CreateLobbyForm, JoinLobbyForm
from app.extensions import db

bp = Blueprint('lobbies', __name__)

@bp.route('/dashboard')
@login_required
def dashboard():
    create_form = CreateLobbyForm()
    join_form = JoinLobbyForm()
    user_lobbies = LobbyMember.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', create_form=create_form, join_form=join_form, user_lobbies=user_lobbies)

@bp.route('/create', methods=['POST'])
@login_required
def create():
    form = CreateLobbyForm()
    if form.validate_on_submit():
        code = uuid.uuid4().hex[:8].upper()
        lobby = Lobby(invite_code=code, host_id=current_user.id)
        db.session.add(lobby)
        db.session.commit()
        
        member = LobbyMember(user_id=current_user.id, lobby_id=lobby.id)
        db.session.add(member)
        db.session.commit()
        
        flash(f'Lobby created successfully with code: {code}', 'success')
        return redirect(url_for('lobbies.view_lobby', lobby_id=lobby.id))
    return redirect(url_for('lobbies.dashboard'))

@bp.route('/lobby/<int:lobby_id>')
@login_required
def view_lobby(lobby_id):
    lobby = Lobby.query.get_or_404(lobby_id)
    is_member = LobbyMember.query.filter_by(user_id=current_user.id, lobby_id=lobby.id).first()
    if not is_member:
        flash('Access denied to this lobby.', 'danger')
        return redirect(url_for('lobbies.dashboard'))
    return render_template('lobby.html', lobby=lobby)
