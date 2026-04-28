from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    registration_deadline = db.Column(db.DateTime, nullable=False)
    max_participants = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    registrations = db.relationship('Registration', backref='event', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Event {self.title}>'

    @staticmethod
    def create(data):
        """建立新活動"""
        new_event = Event(**data)
        db.session.add(new_event)
        db.session.commit()
        return new_event

    @staticmethod
    def get_all():
        """獲取所有活動"""
        return Event.query.all()

    @staticmethod
    def get_by_id(event_id):
        """依 ID 獲取活動"""
        return Event.query.get(event_id)

    def update(self, data):
        """更新活動資訊"""
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()
        return self

    def delete(self):
        """刪除活動"""
        db.session.delete(self)
        db.session.commit()
