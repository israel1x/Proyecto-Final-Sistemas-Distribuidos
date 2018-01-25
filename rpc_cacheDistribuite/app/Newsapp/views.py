import sys
import glob
import redis
from django.shortcuts import render
from django.http import HttpResponse
from app.Newsapp.models import New


sys.path.append('microservice/gen-py')
sys.path.insert(0, glob.glob('/home/josealcivar/Descargas/thrift-0.11.0/lib/py/build/lib*')[0])

from microservice import Toptennews
#from service.ttypes import InvalidOperation, Operation, Work

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol




def main():


    #client.ping()
    print('ping() client')

    #client.getnewsmysql()
    #print(client.getnewsmysql())



def index(request):

    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Toptennews.Client(protocol)

    # Connect!
    transport.open()


    #noticias = New.objects.all()
    noticias=client.getnewsmysql()

    # Close!
    transport.close()

    context = {'noticias': noticias}
    print ("noticias de la base")
    main()
    #return render(request, 'index.html', noticias)
    #return HttpResponse("Index News se presenta las noticias top 10")
    return render(request, "index.html", context)
