#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq.asaf-bar-lev.svc.cluster.local'))
channel = connection.channel()


channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body="www.gov.il,10")
channel.basic_publish(exchange='', routing_key='hello', body="www.pmo.gov.il,10]")
channel.basic_publish(exchange='', routing_key='hello', body="www.police.gov.il,10]")
channel.basic_publish(exchange='', routing_key='hello', body="www.president.gov.il,10]")
channel.basic_publish(exchange='', routing_key='hello', body="www.shabak.gov.il,10]")
channel.basic_publish(exchange='', routing_key='hello', body="www.mossad.gov.il,10]")

print(" [x] Queue initialized")
connection.close()
