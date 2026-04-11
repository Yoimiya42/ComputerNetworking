# Chapter 3 Transport Layer


## 3.1 Introduction and Transport-Layer Services

Provide **logical communication** between **processes** running on different hosts. Whereas network-layer provides logical communication between **hosts**.

### Transport-layer Protocols: TCP vs UDP
TCP (Transmission Control Protocol):
- Reliable, in-order delivery
- Congestion control
- Flow control
- Connection-oriented

UDP (User Datagram Protocol):
- Unreliable, unordered delivery
- No-frills, minimal transport-layer protocol

Sender: breaks app messages into **segments**, passes to network layer as **datagrams**.
Receiver: reassemble segments into messages, pass to application-layer.

---

## 3.2 Multiplexing and Demultiplexing
