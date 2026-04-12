from socket import *

BUFFER_SIZE = 2048

# 1. Create a listening TCP server socket.
server_hostname = ''
server_port = 12000
listen_socket = socket(AF_INET, SOCK_STREAM)
listen_socket.bind((server_hostname, server_port))
    # bind the socket to a port

# 2. Wait for incoming connection requests from clients.
backlog = 1 # the maximum number of queued connections
listen_socket.listen(backlog)

while True:
    # 3. Receive a connection request, and create a dedicated TCP socket to this particular client.
    connection_socket, client_address = listen_socket.accept()

    # 4. Wait for a request from client_socket via connection_socket.
    sentence = connection_socket.recv(BUFFER_SIZE).decode()
    modified_sentence = sentence.upper()

    # 5. Send the response back.
    connection_socket.send(modified_sentence.encode())

    # 6. Close the connection socket.
    connection_socket.close()