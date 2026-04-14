# Chapter 3 Transport Layer

## 3.1 Introduction and Transport-Layer Services

The transport layer provides **logical communication** between **processes** running on different hosts, whereas the network layer provides logical communication between **hosts**.

### Transport-layer Protocols: TCP vs UDP

**TCP (Transmission Control Protocol)**

- Reliable, in-order delivery
- Congestion control
- Flow control
- Connection-oriented

**UDP (User Datagram Protocol)**

- Unreliable, unordered delivery
- A minimal, no-frills transport-layer protocol

On the sender side, the transport layer breaks application messages into **segments** and passes them to the network layer as **datagrams**. On the receiver side, it reassembles segments into messages and passes them to the application layer.

---

## 3.2 Multiplexing and Demultiplexing

### Multiplexing (Sender):

1. Each process passes its message through its own socket.
2. The transport layer wraps each message into a **segment**, attaching the **source port** and **destination port** in the header.
3. Each segment is passed to the network layer, which encapsulates it into an **IP datagram** and sends it to the destination.

<img src="./Multiplexing.png" alt="Multiplexing" width="60%">

### UDP Demultiplexing (Receiver):

The destination socket is identified by the **2-tuple (dst IP, dst port)**.

1. The transport layer receives a segment from the network layer.
2. It inspects the destination port field.
3. It locates the matching server socket and places the data into its receive queue.
4. The process calls `recvfrom()` to retrieve the data and obtain the sender's address for replying.

Segments with different source IP/port pairs but the same destination IP/port are delivered to the same socket.

<img src="./UDP_demultiplexing.png" alt="UDP demultiplexing" width="60%">

### TCP Demultiplexing (Receiver):

The destination socket is identified by the **4-tuple (src IP, src port, dst IP, dst port)**.

1. The transport layer receives a segment from the network layer.
2. It inspects the 4-tuple `(src IP, src port, dst IP, dst port)`.
3. It tries to match the segment against all existing connection sockets.
   - If it is a new request and no match is found:
     - deliver it to the listening socket
     - complete the three-way handshake
     - `accept()` creates a new connection socket and records the 4-tuple
   - If it belongs to an existing connection:
     - deliver it to the matching connection socket
4. The process calls `recv()` to retrieve the data.

<img src="./TCP_demultiplexing.png" alt="TCP demultiplexing" width="60%">

---

# User Datagram Protocol (UDP)

## 3.3 Connectionless Transport: UDP

**UDP (User Datagram Protocol)**  
Reference: [RFC 768 - User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768)

1. **Connectionless**: No handshake is required before sending.
2. **Unreliable**: No guaranteed delivery, ordering, or retransmission.
3. **Best effort**: UDP provides **no congestion control** and **no flow control**, but it is still widely used for applications that can tolerate loss and do not require ordering, such as streaming media, online gaming, and DNS.

### UDP Segment Format

<img src="./UDP_format.png" alt="UDP segment format" width="75%">

### Checksum:

1. Sum all 16-bit words and wrap any overflow back to the least significant bit.
2. Take the one's complement (flip all bits).

Example:

<img src="./checksum.png" alt="Checksum example" width="50%">

--- 

# Transport-Layer Protocols (TCP)

## Reliable Data Transfer (3.4 & 3.5.4)

Core mechanisms for reliable data transfer implemented by TCP:

1. **Error Detection (Checksum)**: The TCP checksum is computed over 16-bit words with overflow wrapped around, and then converted using one's complement. The calculation includes:
   - `Pseudo header` (source IP, destination IP, protocol type, and TCP segment length), which participates in the calculation but is not transmitted
   - `TCP segment header`
   - `TCP segment payload`

   The checksum can detect bit corruption but cannot correct it. The receiver sums the three fields above together with the received checksum. If the result is not all 1s, the segment is considered corrupted and is discarded.

2. **Sequence Numbers and Acknowledgements**: TCP treats data as a continuous **byte stream**.
   - Sequence number: the position of the **first byte of the payload**, starting from the ISN (Initial Sequence Number)
   - Acknowledgement number (cumulative): ACK `N` means the receiver has received all bytes up to `N - 1` and is expecting bytes starting from `N`
   - Both sides can send data and acknowledgements in the same segment, enabling full-duplex communication and piggybacking

   This mechanism solves three problems:
   - detecting duplicates
   - handling out-of-order arrival by buffering and waiting for missing segments
   - handling lost segments through fast retransmission or retransmission after a timeout

3. **Fast Retransmit**: If the sender receives three duplicate ACKs, it assumes the segment is lost and retransmits it immediately, without waiting for the timeout.
4. **Timer and Retransmission**: The sender keeps a timer for the oldest unacknowledged segment. If the timer expires, it retransmits the segment and restarts the timer.
5. **Pipelining**: Multiple unacknowledged segments can be in flight at the same time, improving bandwidth utilization and throughput. The amount of outstanding data is limited by `flow control` and `congestion control`.

## TCP Segment Format (3.5.2)

## RTT Estimation and Timeout (3.5.3)

## TCP Flow Control (3.5.5)

## Connection-oriented Transport: TCP  (3.5.6)

## TCP Congestion Control (3.6 & 3.7)
