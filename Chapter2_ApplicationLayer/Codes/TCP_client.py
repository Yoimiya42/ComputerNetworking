from socket import *

BUFFER_SIZE = 2048

server_hostname = 'localhost'
server_port = 12000
server_address = (server_hostname, server_port)

# 1. Create a client socket that uses TCP protocol.
client_socket = socket(AF_INET, SOCK_STREAM)
    # SOCK_STREAM: socket type for TCP.

# 2. Perform the TCP three-way handshake to establish a TCP connection with the server.
client_socket.connect(server_address)

# 3. Send request to the server_socket via client_socket.
sentence = input('Input lowercase sentence: ')
client_socket.send(sentence.encode()) # no need to attach destination address, since the client socket is already connected to the server socket.

# 4. Wait for the server to respond.
modified_sentence = client_socket.recv(BUFFER_SIZE).decode()
    # Characters continue to accumulate into the buffer until the line ends with a carriage return and newline (\r\n).

print('From Server: ', modified_sentence)

# 5. Close the socket.
client_socket.close()