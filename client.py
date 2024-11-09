import grpc
import greeting_pb2
import greeting_pb2_grpc

def run(key):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeting_pb2_grpc.GreetingServicerStub(channel)
        response = stub.Greet(greeting_pb2.GreetRequest(greetMessage=key))
    # print(f"Result: {response.result}")
    print(response.message)

if __name__ == '__main__':
    # Get user Input 
    key = input("Please type any key: ")
    run(key)