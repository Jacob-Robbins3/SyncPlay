import os
from flask import Flask
from config import Config
from app.extensions import db, login_manager, csrf

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    os.makedirs(os.path.join(app.root_path, '../instance'), exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    from app.auth.routes import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.lobbies.routes import bp as lobbies_bp
    app.register_blueprint(lobbies_bp, url_prefix='/lobbies')

    from app.voting.routes import bp as voting_bp
    app.register_blueprint(voting_bp, url_prefix='/voting')

    @app.route('/')
    def index():
        from flask import render_template
        return render_template('index.html')

    with app.app_context():
        db.create_all()

    return app
