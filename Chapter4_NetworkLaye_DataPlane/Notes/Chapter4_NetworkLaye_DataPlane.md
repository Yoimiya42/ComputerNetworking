# Chapter 4 Network Layer: Data Plane

## Contents:

## 4.1 Overview of Network Layer

Transport segments between **hosts**:
- **sender**: encapsulates segments into datagrams, passes to link layer.
- **receiver**: delivers segments to transport layer protocol.
Network-layer protocols in every Internet devices: **hosts** and **routers**

Network-layer functions:
- **Data Plane**: **local**, pre-router function
  - **forwarding**: **router-local action** of transferring a packet from router's input link to appropriate output link.
- **Control Plane**: **network-wide** logic
  - **routing**: **network-wide process** that determines the end-to-end paths that packets take from src to dst. two control-plane approaches:
    - **traditional routing algorithms**， implemented in routers.
    - **software-defined networking (SDN)**: implemented in (remote) servers

Network-layer service model: **best-effort**
No guarantees on:
 - successful datadgram delivery
 - timing or order of delivery
 - bandwidth available to end-to-end flow

---

## 4.2  Router

---

## 4.3  The Internet Protocol (IP)

---

## 4.4  Forwarding


## 4.5 Middleboxes
1
2
