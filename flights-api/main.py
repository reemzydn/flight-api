from flask import Flask, jsonify, request
from models import Vol

app = Flask(__name__)

flights = []

@app.route('/flights', methods=['GET'])
def get_flight():
    return jsonify([vol.to_dict() for vol in flights])
    
@app.route('/flights/<id>', methods=['GET'])
def get_flights(id):
    for flight in flights:
        if flight.id == int(id):
            return jsonify(flight.to_dict())
    return jsonify({'error': 'Flight not found'}), 404

@app.route('/flights', methods=['POST'])
def add_flight():
    data = request.get_json()
    new = Vol(
        id = len(flights)+1,
        destination = data['destination'],
        prices = data['prices'],
        places = data['places']
    )
    flights.append(new)
    return jsonify({'new flight': 'New flight added.'})

@app.route('/flights/<id>', methods=['DELETE'])
def delete_flight(id):
    for flight in flights:
        if flight.id == int(id):
            flights.remove(flight)
            return jsonify({'remove': 'Flight removed.'})
    return jsonify({'error': 'Flight not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
