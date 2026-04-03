
class Checkin:
    def __init__(self, id, passenger, passport_nb, flight_id):
        self.id = id
        self.passenger = passenger
        self.passport_nb = passport_nb
        self.flight_id = flight_id
        
    def to_dict(self):
        return {
            "id": self.id,
            "passenger": self.passenger,
            "passport nb": self.passport_nb,
            "flight Id": self.flight_id,
        }
        