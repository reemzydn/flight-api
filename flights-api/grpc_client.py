import grpc
import flight_pb2
import flight_pb2_grpc

# Client gRPC pour tester la communication avec le serveur gRPC de flight-api
# Se connecte au port 50051 et appelle la méthode GetFlights
# qui retourne la liste de tous les vols stockés dans la base de données
# C'est l'équivalent du GET /flights en REST mais via le protocole gRPC (binaire, plus rapide)

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = flight_pb2_grpc.FlightServiceStub(channel)
    
    # Test GetFlights
    response = stub.GetFlights(flight_pb2.Empty())
    print("Tous les vols:")
    for flight in response.flights:
        print(f"  id={flight.id}, destination={flight.destination}, prix={flight.prices}")

if __name__ == '__main__':
    run()