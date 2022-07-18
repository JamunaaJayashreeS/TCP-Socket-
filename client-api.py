# Import statements
import socket

# Initializing variables
SocketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9001

print('Waiting for server connection... ')
try:
    SocketClient.connect((host, port))
except socket.error as err:
    print(str(err))

 #https://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php 

file_name = input('Enter the file name : ')
SocketClient.send(str.encode(file_name))
http_response = SocketClient.recv(1024)
response = SocketClient.recv(1024)
print('Response received from server')
response = response.decode('utf-8')
print(response)

# Writing the contents and saving the file in client side
if(response != "404 Not Found"):
    file = open('New ' + file_name, "w")
    file.write(response + " Received from server")
    file.close()
SocketClient.close()
