from fastapi import FastAPI
import grpc
import services_pb2_grpc
import services_pb2
import redis
import time

app = FastAPI()

# Configurar el canal gRPC
channel = grpc.insecure_channel('grpc_server:50051')
stub = services_pb2_grpc.TareaServiciosStub(channel)

# Configurar Redis
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

CACHE_EXPIRY = 60  # Tiempo de expiración en segundos

@app.get("/urls")
def get_all_urls():
    cache_key = 'all_urls'
    cached_data = redis_client.get(cache_key)
    
    if cached_data:
        return {"urls": cached_data.split(',')}
    
    start_time = time.time()
    response = stub.GetAll(services_pb2.Nada())
    elapsed_time = time.time() - start_time
    
    urls = [url.title for url in response.urls]
    redis_client.setex(cache_key, CACHE_EXPIRY, ','.join(urls))
    
    print(f"Tiempo de resolución por computo: {elapsed_time:.2f} segundos")
    return {"urls": urls}

@app.get("/urls/{id}")
def get_url(id: int):
    cache_key = f'url_{id}'
    cached_data = redis_client.get(cache_key)
    
    if cached_data:
        return {"urls": cached_data.split(',')}
    
    start_time = time.time()
    response = stub.Get(services_pb2.UrlId(id=id))
    elapsed_time = time.time() - start_time
    
    urls = [url.title for url in response.urls]
    redis_client.setex(cache_key, CACHE_EXPIRY, ','.join(urls))
    
    print(f"Tiempo de resolución por computo: {elapsed_time:.2f} segundos")
    return {"urls": urls}
