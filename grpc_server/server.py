import grpc
from concurrent import futures
import services_pb2_grpc
import services_pb2

class TareaServicios(services_pb2_grpc.TareaServiciosServicer):
    def GetAll(self, request, context):
        # Implementar lógica aquí
        return services_pb2.Urls(urls=[])

    def Get(self, request, context):
        # Implementar lógica aquí
        return services_pb2.Urls(urls=[])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_TareaServiciosServicer_to_server(TareaServicios(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
