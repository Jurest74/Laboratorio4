import pika

with open("./ip.txt","r") as archivo:
    for linea in archivo:
        ip = linea
        
with open("./puerto.txt","r") as archivo:
    for linea in archivo:
        puerto = linea

connection = pika.BlockingConnection(pika.ConnectionParameters(ip, puerto, '/',
pika.PlainCredentials('jurest74', 'cxaVLQ87')))
channel = connection.channel()
channel.basic_publish(exchange='my_exchange', routing_key='test', body='caminar,jurest74,jurest74@eafit.edu.co')
print("Runnning Producer Application...")
print(" [x] Sent 'Hello World...!'")
connection.close() 