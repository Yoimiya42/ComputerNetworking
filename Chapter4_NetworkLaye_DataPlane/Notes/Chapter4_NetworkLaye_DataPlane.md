# Chapter 4 Network Layer: Data Plane

## Contents

- [Chapter 4 Network Layer: Data Plane](#chapter-4-network-layer-data-plane)
  - [Contents](#contents)
  - [4.1 Overview of Network Layer](#41-overview-of-network-layer)
  - [4.2 Router](#42-router)
    - [Router Architecture](#router-architecture)
    - [Input Port](#input-port)
    - [Switching Fabric](#switching-fabric)
  - [4.3 The Internet Protocol (IP)](#43-the-internet-protocol-ip)
    - [IPv4 Datagram Format](#ipv4-datagram-format)
    - [IPv4 Addressing](#ipv4-addressing)
    - [CIDR: Classless Inter-Domain Routing](#cidr-classless-inter-domain-routing)
    - [DHCP: Dynamic Host Configuration Protocol](#dhcp-dynamic-host-configuration-protocol)
    - [NAT: Network Address Translation](#nat-network-address-translation)
    - [IPv6 Datagram format](#ipv6-datagram-format)
    - [Transitioning from IPv4 to IPv6](#transitioning-from-ipv4-to-ipv6)
  - [4.4 Forwarding](#44-forwarding)
    - [Generalized Forwarding (**Match+Actions**)](#generalized-forwarding-matchactions)
    - [Matches](#matches)
    - [Actions](#actions)
    - [OpenFlow Abstractions](#openflow-abstractions)
  - [4.5 Middleboxes](#45-middleboxes)

## 4.1 Overview of Network Layer

Transport segments between **hosts**:

- **sender**: encapsulates segments into datagrams, passes to link layer.
- **receiver**: delivers segments to transport layer protocol.

Network-layer protocols run in every Internet device: **hosts** and **routers**.

Network-layer functions:

- **Data Plane**: **local**, per-router function.
  - **forwarding**: **router-local action** of transferring a packet from router's input link to appropriate output link.
- **Control Plane**: **network-wide** logic.
  - **routing**: **network-wide process** that determines the end-to-end paths that packets take from source to destination. Two control-plane approaches:
    - **traditional routing algorithms**: implemented in routers.
    - **software-defined networking (SDN)**: implemented in (remote) servers.

Network-layer service model: **best-effort**.

No guarantees on:

- Successful datagram delivery.
- Timing or order of delivery.
- Bandwidth available to an end-to-end flow.

---

## 4.2 Router

### Router Architecture

|Components|Main Functions|Plane|
|----------|-------------|-----|
|Input port|1. Process link-layer frames; 2. Lookup output interface; 3.Queuing|Data|
|Switching fabric| Transfer Packets from input to output|Data|
|Output port|1. Packet scheduling; 2.Encapsulation; 3.Transmit|Data|
|Routing Processor|1. Run routing algorithms; 2. Maintain routing table|Control|

### Input Port
1. **Physical-Layer Processing**: recover bits from incoming signals.
2. **Link-layer Processing**: process the frame and extract the IP datagram.
3. **Lookup**: math the destination IP address against the forwarding table with the **Longest Prefix Matching**.
4. **Queuing**: a queued packet must wait for transfer through the fabric (even though its output port is free) because of **Head Of the Line(HOL) Blocking** (another packet blocks the front of its input queue).
5. **Forwarding**: transfer the packet through the fabric to the appropriate output port.

### Switching Fabric

![Switching Fabric](/Chapter4_Network

Laye_DataPlane/Pictures/switching_techniques.jpg)

---

## 4.3 The Internet Protocol (IP)

### IPv4 Datagram Format

![IP Datagram Format](../Pictures/IP_datagram_format.jpg)

**Interface**: connection between a **host/router** and a **physical link**.

- A router may have **multiple** interfaces, each connected to a different link.
- A host typically has one or two interfaces (**wired Ethernet**, **wireless Wi-Fi**).

IP addresses are associated with each interface.

### IPv4 Addressing

IP address: **subnet portion** + **host portion**.

**Subnet** (IP network): interfaces can physically reach each other **without an intervening router**.

### CIDR: Classless Inter-Domain Routing

**Address notation**:

```math
\underbrace{a.b.c.d}_{\text{IPv4 address}} / \underbrace{x}_{\text{prefix length}}
```

- $a, b, c, d$: the four octets of the IPv4 address, each ranging from $0$ to $255$.
- $x$: number of bits in the **subnet portion**, where $0 \le x \le 32$.
- $32 - x$: number of bits in the **host portion**.

**Address structure** (32 bits in total):

```math
\underbrace{\boxed{\text{Subnet portion}}}_{x\text{ bits}}
\quad\Big|\quad
\underbrace{\boxed{\text{Host portion}}}_{(32-x)\text{ bits}}
```

**Subnet mask**:

```math
\text{Subnet mask} =
\underbrace{11\cdots1}_{x\text{ ones}}
\,\underbrace{00\cdots0}_{(32-x)\text{ zeros}}
```

### DHCP: Dynamic Host Configuration Protocol

![DHCP](../Pictures/DHCP_server_client.jpg)

### NAT: Network Address Translation

**Private IP address + original port** → **NAT device** → **Public IP address + mapped port**

![NAT](../Pictures/NAT.jpg)

### IPv6 Datagram format
![IPv6 Datagram Format](/Chapter4_NetworkLaye_DataPlane/Pictures/IPv6_format.jpg)

16bits * 8 groups(each group has 4 hexadecimal digits)

### Transitioning from IPv4 to IPv6
![Transitioning from IPv4 to IPv6](/Chapter4_NetworkLaye_DataPlane/Pictures/Tunneling.jpg)

---

## 4.4 Forwarding

### Generalized Forwarding (**Match+Actions**)
Flow table in OpenFlow:
1. Priority number
2. **Match** conditions (fields in packet headers)
3. **Actions** to be taken
4. Counters

### Matches
![Matching Fields](/Chapter4_NetworkLaye_DataPlane/Pictures/matching_fields.png)

### Actions
- Forwarding (destination-based forwarding)
- Dropping 
- Modifying fields
- Encapsulating and forwarding to a controller
  
### OpenFlow Abstractions
||Match|Actions|
|:-:|:-:|:-:|
|Router|Longest Des IP prefix| Forward out a link|
|Switch (Layer-2 switching)|Destination MAC address|forward or flood|
|**Firewall**|Src/Des IP addresses / port numbers, protocols|Permit / Deny|
|**NAT**| Source IP address & port (LAN)|Translate IP address & port (WAN)|
|Load Balancing|Src/Des IP addresses/port numbers|Forwarding to different paths/servers|

---

## 4.5 Middleboxes
