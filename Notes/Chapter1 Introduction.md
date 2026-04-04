# Chapter 1 Introduction

Roadmap:
- 1.1 Overview
- 1.2 Network Edge 
  - Access Network:
    - Home: DSL, Cable, Fiber-to-the-Home(FTTH), 5G fixed wireless
    - Public-area: Ethernet, WiFi
    - Wide-area: 4G, 5G
  - Physical Media
- 1.3 Network Core
  -  Packet Switching vs Circuit Switching
  -  Network of networks
- 1.4 Delay, Loss, and Throughput
- 1.5 Protocol Layers


## 1.1 Overview
**end systems <--> hosts**  connected by 
- **communication links** (different physical media)
- **packet switches** (link-layer switches & routers)
run network protocols to exchange messages:
- **Transmission Control Protocol (TCP)**
- **Internet Protocol (IP)**

protocols define **format**, **order** of exchanged messages, **actions** taken on message transmission

## 1.2 Network Edge

### Access Network
#### Residential Access
1. Digital Subscriber Line(DSL)
   - make use of *telephone company's existing local telephone infrastructure*
   - translate between digital data and analog signals by *DSL modem* and *DSL access Multiplexer(DSLAM)*
   - voice and data transmitted at different frequencies over **dedicated** line to centre office
2. Cable Internet Access
   - make use of *cable television company's existing cable television infrastructure*
   - translate between digital data and analog signals by *cable modem* and *cable modem termination system(CMTS)*
   - TV and data transmitted at different frequencies over **shared** cable distribution network

Their access networks are **asymmetric**: high-speed downstream and low-speed upstream
3. Fiber to the Home(FTTH)
   - provide an optical fiber path from the centre office directly to each home
   - two optical-distribution architectures: **Active Optical Network(AON)** and **Passive Optical Network(PON)**
   - PON path:
     router(access the Internet via it) <---> ONT <--(dedicated optical fiber)--> splitter(combine a number of homes) <---> OLT(provide conversion between optical and electrical signals)

4. 5G Fixed Wireless
#### Public-area Access
Local area network(LAN):
- wired LAN: **Ethernet**
- wireless LAN: **WiFi**
#### Wide-area Access
4G, 5G cellular access networks
- send/receive packets through **base stations** that is operated by cellular network provider

### Physical Media
guided media: signals are guided along a solid medium:
- **twisted-pair copper wire**: dial-up modem, DSL, Ethernet cable
- **coaxial Cable**: cable TV, cable Internet access
- **fiber optics**: broadband, long-distance communication
unguided media: signals are propagated in atmosphere or outer space:
- **Terrestrial radio**
  - short distance: Bluetooth
  - local-area: wireless LAN
  - wide-area: cellular access
- **Satellite radio**: geostationary satellites and low-earth orbiting(LEO) satellites

## 1.3 Network Core
### Packet Switching vs Circuit Switching
- Packet switching:
  - **store and forward**: entire packet must receive before it can be transmitted onto outgoing link
  - **output buffer(queue)**: packets wait in buffer until link available -> **queuing delay**
  - **packet loss**: packets may be dropped if buffer is full
  - **statistical multiplexing**: share link among multiple users -> efficient use of link
  - **forwarding table**: map destination address to router's outbound link
- Circuit switching:
  - **dedicated circuit** is reserved for entire duration of communication session
  - resources are **not shared** and wasteful during **silent periods**
  - Multiplexing methods:
    - **Frequency-division multiplexing(FDM)**: each user is allocated a specific frequency band
    - **Time-division multiplexing(TDM)**: each user is allocated a unique time slot in every frame
### Network of networks

**ISP(Internet Service Provider)**: provide either wired or wireless access(DSL, cable, FTTH, WiFi and cellular) to end systems
**PoP(point of presence)**: a group of routers in a specific geographical area where customers can connect into the provider's network
**multi-home**: an ISP connect to multiple provider ISPs for reliability and load balancing
**peering**: multiple nearby ISPs at the same level exchange traffic directly without having to pay a third party ISP
**IXP(Internet Exchange Point)**: a physical infrastructure where multiple ISPs can peer together  

**Tier-1 ISP**: at the highest level, for national or international coverage
**content provider network**: Internet enterprises own and operate their private network that connects its data centers to Internet, bypassing tier-1 and regional ISPs

## 1.4 Delay, Loss, and Throughput
### Types of delays
**Processing delay**: time to examine packet's header and destination, check for bit-level errors.
**Queue delay**: wait to be transmitted onto outgoing link, depends on congestion level of queue.
**Transmission delay**: time push out all bits of packet into link.  
$$\text{Transmission delay} = \frac{L \; (\text{packet length in bits})}{R \; (\text{transmission rate / link bandwidth in bits/s})}$$

**Propagation delay**: time to propagate bits from the beginning of the link to the router.
$$\text{Propagation delay} = \frac{d \; (\text{length of physical link})}{s \; (\text{propagation speed} \approx 2 \times 10^8 \text{ m/s})}$$

total nodal delay:
$$d_{nodal} = d_{proc} + d_{queue} + d_{trans} + d_{prop}$$

### Traffic intensity
a = average rate at which packets arrive at the queue (packets/sec)
L = packet length (bits)

$$\text{Traffic intensity} = \frac{La}{R}$$
![traffic intensity](traffic_intensity.png)

La/R ~ 0: average queueing delay is small.
La/R ~ 1: average queueing delay gets larger and larger.
La/R > 1: *average rate at which bits arrive* >> *rate at which bits can be transmitted from the queue* -> **queue will increase without bound and queuing delay will approach infinity**. 

If the queue is full, arriving packets will be dropped -> **packet loss**.

### Throughput
rate at which bits transferred between sender/receiver
- **instantaneous**: rate at a given point in time
- **average**: rate over longer period of time

**bottleneck link**: $\min\{R_1, R_2, \ldots, R_n\}$

## 1.5 Protocol Layers

**application layer**: provides network services to user-end applications -> **packet**
  - HTTP, FTP, SMTP, DNS 
  
**transport layer**: transports application layer messages between applications endpoints -> **segment**
  - TCP, UDP


**network layer**: routing of network-layer packets from source to destination -> **datagram**
  - IP, routing protocols


**link layer**: data transfer between neighboring network elements -> **frame**
  - Ethernet, WiFi


**physical layer**: individual bits within the frame from one node to the next
  - transmission medium like fiber optic, copper wire, radio
