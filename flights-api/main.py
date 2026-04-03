from flask import Flask, jsonify, request
from models import db, Vol

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flightuser:flight1234@mysql/flight_db'
db.init_app(app)

with app.app_context():
    db.create_all()
    
# flights = []

@app.route('/flights', methods=['GET'])
def get_flights():
    flights = Vol.query.all()
    return jsonify([vol.to_dict() for vol in flights])
    
@app.route('/flights/<id>', methods=['GET'])
def get_flight(id):
    vol = Vol.query.get(int(id))
    if vol:
        return jsonify(vol.to_dict())
    return jsonify({'ERROR': 'Flight not found.'}), 404

@app.route('/flights', methods=['POST'])
def add_flight():
    data = request.get_json()
    new = Vol(
        # id = len(flights)+1,
        destination = data['destination'],
        prices = data['prices'],
        places = data['places']
    )
    db.session.add(new)
    db.session.commit()
    # flights.append(new)
    return jsonify({'New Flight': 'New flight added.'})

@app.route('/flights/<id>', methods=['DELETE'])
def delete_flight(id):
    vol = Vol.query.get(int(id))
    if vol:
        db.session.delete(vol)
        db.session.commit()
        return jsonify({'Remove': 'Flight removed.'})
    # for flight in flights:
    #     if flight.id == int(id):
    #         flights.remove(flight)
    #         return jsonify({'remove': 'Flight removed.'})
    return jsonify({'ERROR': 'Flight not found.'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
