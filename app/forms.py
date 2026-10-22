from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class CreateLobbyForm(FlaskForm):
    submit = SubmitField('Create New Lobby')

class JoinLobbyForm(FlaskForm):
    invite_code = StringField('Invite Code', validators=[DataRequired(), Length(min=4, max=16)])
    submit = SubmitField('Join Lobby')
