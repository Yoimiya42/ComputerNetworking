# Chapter 1: Introduction to Computer Networking

>R1. What is the difference between a host and an end system? List several different types of end systems. Is a Web server an end system?
- The term *host* and *end system* are often used interchangeably. They both refer to the devices connected to the network that run application programs.
- The term *host* emphasizes the fact that these devices run application programs, while *end system* highlights their position at the "end" of the network, as opposed to the intermediate devices(like routers and switches) in the middle.
- Examples of end systems include: laptops, tablets, IoT devices, smartphones
- A web server is indeed an end system as it runs a Web server application and communicates with other end systems over the network.

>R9. HFC, DSL, and FTTH are all used for residential access. For each of these access technologies, provide a range of transmission rates and comment on whether the transmission rate is shared or dedicated.
- HFC(Hybrid Fiber Coaxial): 100 Mbps -- 1 Gbps. **Shared.** bandwidth is sharded among homes in the local cable segment.
- DSL (Digital Subscriber Line): 24 Mbps -- 100+ Mbps. **Dedicated.** The copper line from the home to cabinet/CO is an exclusive, point-to-point connection.
- FTTH (Fiber to the home): 100 Mbps -- 10 Gbps. **Shared**(in PON architecture). The total capacity of the fiber is shared among a small group of users via splitter. 
  
>R10. Describe the most popular wireless Internet access technologies today. Compare and contrast them.
- **Wireless Local Area Networks (WLANs)**， primarily powered by **Wi-Fi**.
- **Wireless Wide Area Networks (WWANs)**,  primarily powered by **Cellular (4G LTE/5G)**

| Feature | WLAN (Wi-Fi) | WWAN (Cellular 4G/5G) |
|:---------:|:--------------:|:-----------------------:|
| Coverage Area | **Small (local)**,  tens of meters (indoor)| **Large (Wide-Area)**, kilometers(outdoor)| 
| Mobility | **Low**. Designed for homes, offices, public hotpots | **High**. Designed for mobile access | 
|Speed| **Extremely High**. Up to several Gbps (Wi-Fi 6/6E)| **High**. Up to 1 Gbps (5G) |
|Cost| **Low/Free**. Typically a flat monthly fee for  the wired broadband connection| **High/Subscription**. Charges based on data usage and plan|
|Infrastructure| **User/Enterprise-Owned**. Requires a router/access point connected to a wired ISP | **Service Provider-Owned**. Relies on a vast network of cell towers and base stations|