from flask import Flask, jsonify, request
from models import db, Checkin

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://checkinuser:checkin1234@mysql/checkin_db'
db.init_app(app)

with app.app_context():
    db.create_all()
    print("Tables créées avec succès")
    
# checkins = []

@app.route('/checkin', methods=['GET'])
def get_checkins():
    checkins = Checkin.query.all()
    return jsonify([checkin.to_dict() for checkin in checkins])
    
@app.route('/checkin/<flight_id>', methods=['GET'])
def get_checkin(flight_id):
    checkin = Checkin.query.get(int(flight_id))
    if checkin:
        return jsonify(checkin.to_dict())
    # for checkin in checkins:
    #     if checkin.id == int(flight_id):
    #         return jsonify(checkin.to_dict())
    return jsonify({'ERROR': 'Check-in not found.'}), 404
    
@app.route('/checkin', methods=['POST'])
def add_checkin():
    data = request.get_json()
    new = Checkin(
        # id = len(checkins)+1,
        passenger = data['passenger'],
        passport_nb = data['passport_nb'],
        flight_id = data['flight_id']
    )
    db.session.add(new)
    db.session.commit()
    # checkins.append(new)
    return jsonify({'New Check-In': 'New check-in added.'})

@app.route('/checkin/<id>', methods=['DELETE'])
def delete_checkin(id):
    checkin = Checkin.query.get(int(id))
    if checkin:
        db.session.delete(checkin)
        db.session.commit()
        return jsonify({'Remove': 'Check-in removed.'})
    # for checkin in checkins:
    #     if checkin.id == int(id):
    #         checkins.remove(checkin)
    #         return jsonify({'remove': 'Check-in removed.'})
    return jsonify({'ERROR': 'Check-in not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
