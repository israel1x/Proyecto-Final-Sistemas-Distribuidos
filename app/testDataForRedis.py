#!/usr/bin/env python
# coding: utf-8

import redis

def main():
	r = redis.StrictRedis(host='localhost',port='6379', db=0)
	r.set('15/01/2018','Inundaciones en Peru')
	r.set('16/01/2018','Robo en Costa Rica')
	r.set('17/01/2018','Inundaciones en Guatemala')
	r.set('18/01/2018','Inundaciones en Chile')
	r.set('19/01/2018','Brasil Campeon')
	r.set('20/01/2018','Rusia Industrial')
	r.set('21/01/2018','Ecuador Primero')
	r.set('22/01/2018','Canpaña Ecuado All is you need')
	r.set('23/01/2018','Cuenca la mejor ciudad del Ecuador')
	r.set('24/01/2018','Guayaquil Turistico')
	r.set('25/01/2018','Parque Samanes se Inaguro')
	r.set('26/01/2018','ESPOL primera universidad el Ecuador')
	r.set('27/01/2018','España y Cataluña')
	r.set('28/01/2018','Ecuador el pais mas emprendedor')
	r.set('29/01/2018','Colombia, Argentina y Chile pioneros en tecnologia')
	r.set('1/02/2018','Deslaves en Chile')
	r.set('2/02/2018','Premio de la loteria se acumuló')
	r.set('3/02/2018','Turista se perdio en Galapagos')
	r.set('4/02/2018','Se rescato al turista perdido en Galapagos')
	r.set('5/02/2018','Salinas se prepara para el carnaval')

if __name__ == '__main__':
	main()