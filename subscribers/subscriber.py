import pika
import smtplib

with open("./ip.txt","r") as archivo:
    for linea in archivo:
        ip = linea
        
with open("./puerto.txt","r") as archivo:
    for linea in archivo:
        puerto = linea

connection = pika.BlockingConnection(pika.ConnectionParameters(ip, puerto, '/',
pika.PlainCredentials("jurest74", "cxaVLQ87")))
channel = connection.channel()
def callback(ch, method, properties, body):
 print(f'{body} is received')
 arrayMessage = body.decode().split(',')
 print(arrayMessage)
 print(arrayMessage[0])
 print(arrayMessage[1])
 print(arrayMessage[2])
 emailCustomer = str(arrayMessage[2])
 message = 'Subject: Notificacion\nSe ha ejecutado la accion ' + arrayMessage[0] + ' del usuario ' + arrayMessage[1] + ' con Exito'
 message = str(message)
 print(message)
 conexion = smtplib.SMTP(host='smtp.gmail.com',port=587)
 conexion.ehlo()
 conexion.starttls()
 conexion.login(user='restrepolds30@gmail.com', password= 'cxaVLQ87')
 conexion.sendmail(from_addr='restrepolds30@gmail.com', to_addrs=emailCustomer, msg = message)
 conexion.quit()

channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
channel.start_consuming()