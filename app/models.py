from datetime import datetime
from flask_login import UserMixin
from app.extensions import db, login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    steam_id = db.Column(db.String(64), unique=True, nullable=False)
    display_name = db.Column(db.String(128), nullable=False)
    avatar_url = db.Column(db.String(256), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    lobbies_hosted = db.relationship('Lobby', backref='host', lazy=True)
    memberships = db.relationship('LobbyMember', backref='user', lazy=True)
    votes = db.relationship('GameVote', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.display_name} ({self.steam_id})>'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Lobby(db.Model):
    __tablename__ = 'lobbies'

    id = db.Column(db.Integer, primary_key=True)
    invite_code = db.Column(db.String(16), unique=True, nullable=False)
    host_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    session_lock_time = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    members = db.relationship('LobbyMember', backref='lobby', cascade='all, delete-orphan', lazy=True)
    votes = db.relationship('GameVote', backref='lobby', cascade='all, delete-orphan', lazy=True)

    def __repr__(self):
        return f'<Lobby {self.invite_code}>'

class LobbyMember(db.Model):
    __tablename__ = 'lobby_members'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lobby_id = db.Column(db.Integer, db.ForeignKey('lobbies.id'), nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

class GameVote(db.Model):
    __tablename__ = 'game_votes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lobby_id = db.Column(db.Integer, db.ForeignKey('lobbies.id'), nullable=False)
    game_appid = db.Column(db.Integer, nullable=False)
    game_title = db.Column(db.String(256), nullable=False)
    vote_status = db.Column(db.String(32), default='shortlisted')  # shortlisted, upvoted, vetoed
