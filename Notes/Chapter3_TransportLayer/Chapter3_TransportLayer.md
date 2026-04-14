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
# User Datagram Protocol (UDP)

## 3.3 Connectionless Transport: UDP
UDP (User Datagram Protocol):
Reference: [RFC 768 - User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768)
1. **Connectionless**: no handshakes before sending.
2. **Unreliable**: no guaranteed delivery, no ordering, no retransmission.
3. **Best effort**: UDP does provide **no congestion control**, **no flow control**, but it is still widely used for applications that can tolerate loss and do not require ordering, such as streaming media, online gaming, and DNS.

### UDP Segment Format

<img src="./UDP_format.png" width="75%">     

Checksum:
1. Sum all 16-bit words, wrap overflow back to the least significant bit.
2. Take the one's complement (flip all bits).
Example: 
<img src="./checksum.png" width="50%">

--- 

# Transport-Layer Protocols (TCP)


## 3.4 Reliable Data Transfer
Core Mechanisms for Reliable Data Transfer (implemented by TCP):
1. **Error Detection (Checksum)**: 
 TCP checksum sums in 16-bit words with overflow wrapped around, take the one's complement, including:
    - `Presudo Header` (src/det IP, protocol type, tcp segment length), participating in calculation but not transmitted.
    - `TCP Segment Header`
    - `TCP Segment Payload`
 Checksum is used to detect only but not correct bit corruptions. Receiver sums up above three fields with the checksum received. if the result is not 111..111 (all 1s), the segment is corrupted and is discarded.
2. **Sequence Numbers + Acknowledgements**:
  TCP treats data as a continuous **byte stream**   
  - Sequence number: the position of the **first byte of payload**, start from ISN (Initial Sequence Number)
  - Acknowledgement number (cumulative): ACK N means the receiver has received all bytes up to N-1, and is expecting bytes starting from N.
  - Both fields appear in every segment, enabling full-duplex and piggybacking.
  This mechanism solves three problems: 
    1) detecting duplicate (same seq -> discard), 
    2) handling out-of-order arrival (buffer and wait for missing segments), 
    3) handling lost segments (sender fast retransmit or retransmission after timeout).
3. **Fast Retransmit**: if the sender receives 3 duplicate ACKs. it assumes the segment is lost and retransmits it immediately, without waiting for the timeout.
4. **Timer + Retransmission**: keep a timer for the oldest unacknowledged segment. If the timer expires, retransmit the segment and restart the timer.
5. **Pipeline**: multiple unacknowledged segments can be in flight at the same time, improving bandwidth utilization and throughput.
   
## 3.5 Connection-oriented Transport