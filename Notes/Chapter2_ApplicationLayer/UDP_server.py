from socket import *

BUFFER_SIZE = 2048 # indicates the maximum amount of data to be received at once

# 1. create a server socket that uses UDP protocol
server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port)) 
    # bind the socket to a port
    #'' means listen on all network interfaces (equivalent to 0.0.0.0)

#while loop is used to keep the server running and able to handle multiple client requests sequentially
while True:

    # 2. wait for a message to arrive from client_socket via server_socket.
    message, client_address = server_socket.recvfrom(BUFFER_SIZE)
    modified_message = message.decode().upper()

    # 3. send the response back
    server_socket.sendto(modified_message.encode(), client_address) 
