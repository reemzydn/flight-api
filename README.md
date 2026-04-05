# Commandes utiles du projet

## Prérequis
```bash
minikube start
minikube tunnel  # laisser ce terminal ouvert
```

## API flight-api (REST)

### Ajouter un vol
```bash
curl -X POST http://flight-api.info/flights -H "Content-Type: application/json" -d "{\"destination\": \"Paris\", \"prices\": 200, \"places\": 50}"
```

### Lister tous les vols
```bash
curl http://flight-api.info/flights
```

### Supprimer un vol
```bash
curl -X DELETE http://flight-api.info/flights/1
```

## API checkin-api (REST)

### Ajouter un check-in
```bash
curl -X POST http://flight-api.info/checkin -H "Content-Type: application/json" -d "{\"passenger\": \"Alice\", \"passport_nb\": \"AB123456\", \"flight_id\": 1}"
```

### Lister tous les check-ins
```bash
curl http://flight-api.info/checkin
```

### Supprimer un check-in
```bash
curl -X DELETE http://flight-api.info/checkin/1
```

## MySQL

### Se connecter
```bash
kubectl exec --stdin --tty <nom-pod-mysql> -- mysql -ptest1234
```

### Requêtes utiles
```sql
-- Vols
use flight_db;
select * from flights;
delete from flights where id = 1;

-- Check-ins
use checkin_db;
select * from checkin;
delete from checkin where id = 1;
```

## gRPC

### Port-forward (terminal séparé)
```bash
kubectl port-forward deployment/flight-api 50051:50051
```

### Lancer le client gRPC
```bash
cd flights-api
python grpc_client.py
```

## Istio Service Mesh

### Port-forward vers l'Istio Ingress Gateway (terminal séparé)
```bash
kubectl -n istio-system port-forward deployment/istio-ingressgateway 31380:8080
```

### Tester via Istio
```bash
curl http://localhost:31380/flights
curl http://localhost:31380/checkin
```

### Vérifier les sidecars injectés (2/2)
```bash
kubectl get pods
```

## Sécurisation du cluster

### RBAC
```bash
kubectl apply -f rbac.yaml
kubectl describe pod <nom-pod-flight-api> | findstr "Service Account"
```

### mTLS Istio
```bash
kubectl apply -f mtls.yaml
```

### Vérifier que mTLS est actif
```bash
kubectl get peerauthentication
```

### Istio Gateway
```bash
# Terminal séparé
kubectl -n istio-system port-forward deployment/istio-ingressgateway 31380:8080

# Tester
curl http://localhost:31380/flights
curl http://localhost:31380/checkin
```

### Les images docker
Image flight-api : https://hub.docker.com/r/rimzdn/flights-api
Image checkin-api : https://hub.docker.com/r/rimzdn/checkin-api