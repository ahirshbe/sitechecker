#!/usr/bin/env python
import pika
import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body="www.gov.il,10")
channel.basic_publish(exchange='', routing_key='hello', body="www.pmo.gov.il,10]")
channel.basic_publish(exchange='', routing_key='hello', body="www.police.gov.il,10]")
channel.basic_publish(exchange='', routing_key='hello', body="www.president.gov.il,10]")
channel.basic_publish(exchange='', routing_key='hello', body="www.shabak.gov.il,10]")
channel.basic_publish(exchange='', routing_key='hello', body="www.mossad.gov.il,10]")

channel.queue_declare(queue='hello')
channel.queue_declare(queue='log')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    val = str(body).split(',')
    log_message = "Processed {0!s} at {0!s}".format(val[0], str(datetime.datetime))
    #print(val)
    channel.basic_publish(exchange='', routing_key='hello', body=body)
    channel.basic_publish(exchange='', routing_key='log', body=log_message)
    print(" [x] Sent '%r'" % val)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()