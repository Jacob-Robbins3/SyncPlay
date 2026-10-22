from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import GameVote
from app.extensions import db

bp = Blueprint('voting', __name__)

@bp.route('/vote', methods=['POST'])
@login_required
def cast_vote():
    data = request.get_json()
    lobby_id = data.get('lobby_id')
    game_appid = data.get('game_appid')
    game_title = data.get('game_title')
    status = data.get('status', 'shortlisted')

    vote = GameVote.query.filter_by(user_id=current_user.id, lobby_id=lobby_id, game_appid=game_appid).first()
    if vote:
        vote.vote_status = status
    else:
        vote = GameVote(user_id=current_user.id, lobby_id=lobby_id, game_appid=game_appid, game_title=game_title, vote_status=status)
        db.session.add(vote)
    
    db.session.commit()
    return jsonify({'success': True, 'status': vote.vote_status})
