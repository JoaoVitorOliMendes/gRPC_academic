import grpc
from concurrent import futures
import greeting_pb2
import greeting_pb2_grpc

class GreetingServicer(greeting_pb2_grpc.GreetingServicer):
    def Greet(self, request, context):
        result = request.greetMessage
        return greeting_pb2.GreetResponse(message=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeting_pb2_grpc.add_GreetingServicerServicer_to_server(GreetingServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print("Hello from server!")
    serve()