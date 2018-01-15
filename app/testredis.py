#!/usr/bin/env python
# coding: utf-8

import redis

def main():
	r = redis.StrictRedis(host='localhost',port='6379', db=0)
	r.set('15/01/2018','Inundaciones')
	print r.get('15/01/2018')
	print r.exists('15/01/2018') 


if __name__ == '__main__':
	main()