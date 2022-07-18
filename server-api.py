# Import Statements
import socket
import os
from _thread import *

SocketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Initializing variables
host = '127.0.0.1'
port = 9001
thread_count = 0
http_header = 'HTTP/1.0 200 OK\r\n'
content_type = 'Content-Type: text/html\r\n'

# Server socket creation
try:
    SocketServer.bind((host, port))
except socket.error as err:
    print(str(err))

print('Server is ready/waiting for client request')
SocketServer.listen(4)


def client_connection(connection):
    connection.send(str.encode('Enter the file name : '))
    data = connection.recv(2048)
    if(data != 'No'):
        file_name = data.decode('utf-8')
        try:
            file_object = open(file_name, "r")
        except Exception:
            print("File not found")
            connection.send("404 Not Found".encode())
        else:
            value = http_header + content_type + file_object.read(1024)
            connection.send(value.encode())
            print('Sent value', repr(value))
            file_object.close()
    else:
        connection.close()


while True:
    #https://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php 
    
    Client, client_address = SocketServer.accept()
    print('Connected with: ' +
          client_address[0] + ' Port No: ' + str(client_address[1]))
    start_new_thread(client_connection, (Client, ))
    thread_count += 1
    print('Thread Id: ' + str(thread_count))

SocketServer.close()
