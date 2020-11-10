from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///csv_upload.sqlite3'
db = SQLAlchemy(app)


class Exercise(db.Model):
    __tablename__ = "exercise"
    id            = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(256), unique=True, nullable=False)
    exercise_type = db.Column(db.String(100), unique=False, nullable=True)
    muscle_group  = db.Column(db.String(256), unique=False, nullable=True)
    youtube_link  = db.Column(db.String(256), unique=False, nullable=True)      # turn into unique = true

    def __repr__(self):
        return '<Exercise: %d | %s | %s | %s | %s' % (self.id, self.exercise_name, self.exercise_type, self.body_part, self.youtube_link)
