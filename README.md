# application
``
docker commands:
docker build -t app .
docker run -p 5000:5000 app
``
--------------------------
``
docker-compose commands:
docker-compose up --build
``
----------------------------
K8s commands
'''

kind create cluster --name city-info

kind load docker-image city-info:latest --name city-info
docker build -t city-info .

kubectl apply -f k8s

kubectl port-forward svc/city-info 9000:80

'''