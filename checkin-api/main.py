from flask import Flask, jsonify, request
from models import Checkin

app = Flask(__name__)

checkins = []

@app.route('/checkin', methods=['GET'])
def get_checkins():
    return jsonify([checkin.to_dict() for checkin in checkins])
    
@app.route('/checkin/<flight_id>', methods=['GET'])
def get_checkin(flight_id):
    for checkin in checkins:
        if checkin.id == int(flight_id):
            return jsonify(checkin.to_dict())
    return jsonify({'error': 'Check-in not found'}), 404
    
@app.route('/checkin', methods=['POST'])
def add_checkin():
    data = request.get_json()
    new = Checkin(
        id = len(checkins)+1,
        passenger = data['passenger'],
        passport_nb = data['passport_nb'],
        flight_id = data['flight_id']
    )
    checkins.append(new)
    return jsonify({'New Check-In': 'New check-in added.'})

@app.route('/checkin/<id>', methods=['DELETE'])
def delete_checkin(id):
    for checkin in checkins:
        if checkin.id == int(id):
            checkins.remove(checkin)
            return jsonify({'remove': 'Check-in removed.'})
    return jsonify({'error': 'Check-in not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
