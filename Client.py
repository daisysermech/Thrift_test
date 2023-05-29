from tutorial import MultiplicationService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

transport = TSocket.TSocket('localhost', 9090)

transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = MultiplicationService.Client(protocol)

transport.open()
y = True
while y:
    n1 = int(input())
    n2 = int(input())
    product = client.multiply(n1,n2)
    print(product)
    y = input("Continue?")
transport.close()
