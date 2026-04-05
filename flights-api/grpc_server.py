import grpc
from concurrent import futures
import flight_pb2
import flight_pb2_grpc
from models import db, Vol
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flightuser:flight1234@mysql/flight_db'
db.init_app(app)

class FlightService(flight_pb2_grpc.FlightServiceServicer):
    
    def GetFlights(self, request, context):
        with app.app_context():
            flights = Vol.query.all()
            return flight_pb2.FlightList(
                flights=[flight_pb2.FlightResponse(
                    id=v.id,
                    destination=v.destination,
                    prices=v.prices,
                    places=v.places
                ) for v in flights]
            )
    
    def GetFlight(self, request, context):
        with app.app_context():
            vol = Vol.query.get(request.id)
            if vol:
                return flight_pb2.FlightResponse(
                    id=vol.id,
                    destination=vol.destination,
                    prices=vol.prices,
                    places=vol.places
                )
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return flight_pb2.FlightResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    flight_pb2_grpc.add_FlightServiceServicer_to_server(FlightService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()