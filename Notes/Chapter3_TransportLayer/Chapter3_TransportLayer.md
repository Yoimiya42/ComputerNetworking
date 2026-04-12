# Chapter 3 Transport Layer


## 3.1 Introduction and Transport-Layer Services

Provide **logical communication** between **processes** running on different hosts. Whereas network-layer provides logical communication between **hosts**.

### Transport-layer Protocols: TCP vs UDP

**TCP (Transmission Control Protocol):**

- Reliable, in-order delivery
- Congestion control
- Flow control
- Connection-oriented

**UDP (User Datagram Protocol):**

- Unreliable, unordered delivery
- No-frills, minimal transport-layer protocol

Sender: breaks app messages into **segments**, passes to network layer as **datagrams**.
Receiver: reassemble segments into messages, pass to application-layer.

---

## 3.2 Multiplexing and Demultiplexing

### Multiplexing (Sender):

1. Each process passes its message through its own socket.
2. Transport-layer wraps each message into a **segment**, attaching a **(src port, dst port)** in the header.
3. Each segment is passed to the network-layer, which encapsulates it into an **IP datagram** and sends it to the destination.

<img src="./Multiplexing.png" alt="Multiplexing" width="60%">

### UDP Demultiplexing (Receiver):

The destination socket is identified by: **2-tuple (dst IP, dst port)**.

1. Transport-layer receives a segment from the network-layer.
2. Inspects the destination port field.
3. Locates the matching server socket and places the data into its receive queue.
4. The process calls `recvfrom()` to retrieve the data, and gets the sender's address for replying.

Different source IP/port but the same destination IP/port are delivered to the same single socket.

<img src="./UDP_demultiplexing.png" alt="UDP demultiplexing" width="60%">

### TCP Demultiplexing (Receiver):

The destination socket is identified by: **4-tuple (src IP, src port, dst IP, dst port)**.

1. Transport-layer receives a segment from the network-layer.
2. Inspects the 4-tuple (src IP, src port, dst IP, dst port).
3. Tries to match it against all existing connection sockets.
   - If it is a new request (no match):
     - deliver to the listening socket
     - three-way handshake
     - `accept()` creates a new connection socket with the 4-tuple recorded on it
   - If it is an existing connection (match):
     - deliver to the matching connection socket
4. The process calls `recv()` to retrieve the data.

<img src="./TCP_demultiplexing.png" alt="TCP demultiplexing" width="60%">

---

## 3.3 Connectionless Transport: UDP