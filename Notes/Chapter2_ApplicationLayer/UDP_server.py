from socket import *

'''
1. create a server socket that uses UDP protocol
'''
server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port)) # bind the socket to a port, and '' means listen on all network interfaces (equivalent to 0.0.0.0)


'''
2. wait for a datagram to arrive, then process it and send back to client_socket via the server_socket
while loop is used to keep the server running and able to handle multiple client requests sequentially
'''
buffer_size = 2048 # indicates the maximum amount of data to be received at once
while True:
    message, client_address = server_socket.recvfrom(buffer_size)
    modified_message = message.decode().upper() # convert bytes to string, and convert it to uppercase
    server_socket.sendto(modified_message.encode(), client_address) # convert string to bytes, and send it back to the client via the client's address
