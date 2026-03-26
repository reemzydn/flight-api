
class Vol:
    def __init__(self, id, destination, prices, places):
        self.id = id
        self.destination = destination
        self.prices = prices
        self.places = places
    
    def to_dict(self):
        return {
            "id": self.id,
            "destination": self.destination,
            "prices": self.prices,
            "places": self.places
        }