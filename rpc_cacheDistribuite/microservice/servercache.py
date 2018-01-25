# -*- coding: utf-8 -*-
import glob
import sys
import pymysql
from datetime import datetime
import time
import redis
import cPickle
import hashlib


sys.path.insert(0,'gen-py')
sys.path.insert(0,glob.glob('/home/josealcivar/Descargas/thrift-0.11.0/lib/py/build/lib*')[0])

from microservice import Toptennews
from microservice.ttypes import KVNews
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


redis_server = redis.Redis('localhost')
cnx = pymysql.connect(host='localhost',database='microservice',user='root', password='root')
cursor = cnx.cursor()


class Server():
    def __init__(self):
        self.log = {}



            #obtiene los datos de la base de datos


    def ping(self):
        print('ping() server')



    def getnewsmysql(self):
        listNews=[]

        query = "SELECT * FROM Newsapp_new ORDER BY num_access DESC LIMIT 10"


        cursor.execute(query)
        print "\n"
        startTime = datetime.now()
        print(startTime)
        print "inicia"
        result = self.cache_memory(query)
        stopTime = datetime.now()
        print(stopTime)
        print "termina"
        for row in result:
            print row[0], row[1], row[2], row[3], row[4], row[5]
            listNews.append(KVNews(str(row[1]), str(row[2])))

        return listNews



    def cache_memory(self, query):


        hora_consulta=time.strftime("%H:%M")

        hash = hashlib.sha224(hora_consulta).hexdigest()
        key = "key_cache: " + hash
        print ("Created Key\t : %s" % key)


        #consulta si hay datos en la memoria cache

        if(redis_server.get(key)):
            print "valores alojados en memoria cache son mostrados"
            return cPickle.loads(redis_server.get(key))

        else:
            '''
            ejecuta el query para agreagarlo a la memoria
            '''
            cursor.execute(query)
            data = cursor.fetchall()

            redis_server.set(key, cPickle.dumps(data))
            redis_server.expire(key,360)

            print "se agregaron datos a la memoria cache"
            print "\n devuelve datos directamente de la base de datos"

            return cPickle.loads(redis_server.get(key))

            

    #def stop(self):
    #    self.transport.close()
    #    print('done.')



if __name__ == '__main__':

    handler = Server()
    processor = Toptennews.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Server starting.....!!!")
    server.serve()

#    try:

    #except KeyboardInterrupt:
    #    print("Exit")
    #finally:
    #    server.stop()
    #    sys.exit(0)
