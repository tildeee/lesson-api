from app import db

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title=db.Column(db.String(80))
    description=db.Column(db.Text)
