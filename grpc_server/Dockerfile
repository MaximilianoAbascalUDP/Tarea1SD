FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Compilar archivos .proto (Necesitarás instalar grpcio-tools en requirements.txt)
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. services.proto

CMD ["python", "server.py"]
