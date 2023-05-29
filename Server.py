from tutorial import MultiplicationService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class CalculatorHandler:
    def __init__(self):
        self.log = {}

    def multiply(self, n1, n2):
        print('multiply(%d,%d)' % (n1, n2))
        return n1 * n2

handler = CalculatorHandler()
processor = MultiplicationService.Processor(handler)
transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print('Starting the server...')
server.serve()
print('done.')