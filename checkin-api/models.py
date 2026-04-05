from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Checkin(db.Model):
    __tablename__ = 'checkins'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    passenger = db.Column(db.String(100), nullable=False)
    passport_nb = db.Column(db.String(20), nullable=False)
    flight_id = db.Column(db.Integer, nullable=False)
    
    # def __init__(self, id, passenger, passport_nb, flight_id):
    #     self.id = id
    #     self.passenger = passenger
    #     self.passport_nb = passport_nb
    #     self.flight_id = flight_id
        
    def to_dict(self):
        return {
            "id": self.id,
            "passenger": self.passenger,
            "passport nb": self.passport_nb,
            "flight Id": self.flight_id,
        }
        