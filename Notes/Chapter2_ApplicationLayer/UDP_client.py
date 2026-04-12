from socket import *

server_hostname = 'server_hostname'
server_port = 12000
server_address = (server_hostname, server_port)

'''
1. create a client's socket that uses UDP protocol
AF_INET: address family for IPv4
SOCK_DRAM: socket type for UDP
'''
client_socket = socket(AF_INET, SOCK_DRAM)


message = input('Input lowercase sentence: ')


'''
2. put the message into socket, and send it to the server
'''
client_socket.sendto(
    message.encode(), # convert string to bytes, and put them into socket
    server_address  # destination address
)

'''
3. wait for the server to respond, and receive the modified message and the server's address
'''
buffer_size = 2048 # indicates the maximum amount of data to be received at once
message_modified, server_address = client_socket.recvfrom(buffer_size) 


'''
4. process the received data and close the socket
'''
print('From Server: ', message_modified.decode()) # convert bytes to string, and print it
client_socket.close()