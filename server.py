import grpc
from concurrent import futures
import time

import short_pb2
import short_pb2_grpc

import short

class ShortServicer(short_pb2_grpc.ShortServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def shortURLToId():
        response = short_pb2.shortUrl()
        response.value = short.shortURLToId(request.value)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_ShortServicer_to_server`
# to add the defined class to the server
short_pb2_grpc.add_ShortServicer_to_server(
        ShortServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)