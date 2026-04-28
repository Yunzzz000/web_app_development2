from datetime import datetime
from .event import db

class Registration(db.Model):
    __tablename__ = 'registrations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Registration {self.name} for Event {self.event_id}>'

    @staticmethod
    def create(data):
        """建立新報名"""
        try:
            new_reg = Registration(**data)
            db.session.add(new_reg)
            db.session.commit()
            return new_reg
        except Exception as e:
            db.session.rollback()
            print(f"Error creating registration: {e}")
            return None

    @staticmethod
    def get_by_event(event_id):
        """獲取特定活動的所有報名"""
        try:
            return Registration.query.filter_by(event_id=event_id).all()
        except Exception as e:
            print(f"Error getting registrations for event {event_id}: {e}")
            return []

    @staticmethod
    def get_by_id(reg_id):
        """依 ID 獲取報名資訊"""
        try:
            return Registration.query.get(reg_id)
        except Exception as e:
            print(f"Error getting registration by id {reg_id}: {e}")
            return None

    def delete(self):
        """取消報名"""
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting registration: {e}")
            return False
