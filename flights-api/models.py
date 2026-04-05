from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vol(db.Model):
    # Nom de la table dans la base de données de flight-api
    __tablename__ = 'flights'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    destination = db.Column(db.String(100), nullable=False)
    prices = db.Column(db.Integer, nullable=False)
    places = db.Column(db.Integer, nullable=False)
    
    # Code sans MySQL
    # def __init__(self, id, destination, prices, places):
    #     self.id = id
    #     self.destination = destination
    #     self.prices = prices
    #     self.places = places
    
    # Transformer les données en JSON (le service REST a besoin des données en JSON)
    def to_dict(self):
        return {
            "id": self.id,
            "destination": self.destination,
            "prices": self.prices,
            "places": self.places
        }