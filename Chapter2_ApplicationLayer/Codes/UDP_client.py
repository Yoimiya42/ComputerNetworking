from socket import *

BUFFER_SIZE = 2048 # indicates the maximum amount of data to be received at once

server_hostname = 'localhost' # 127.0.0.1
server_port = 12000
server_address = (server_hostname, server_port)

# 1. create a client socket that uses UDP protocol
client_socket = socket(AF_INET, SOCK_DGRAM)
    # AF_INET: address family for IPv4
    # SOCK_DGRAM: socket type for UDP

# 2. create message, and send it to the server_socket via client_socket
message = input('Input lowercase sentence: ')
client_socket.sendto(message.encode(), server_address)   
    # attach destination address
    # The OS automatically binds the client socket to a port here.

# 3. wait for the server to respond, and receive the modified message and the server's address
message_modified, server_address = client_socket.recvfrom(BUFFER_SIZE)
print('From Server: ', message_modified.decode()) # convert bytes to string, and print it

# 4. close the socket
client_socket.close()
