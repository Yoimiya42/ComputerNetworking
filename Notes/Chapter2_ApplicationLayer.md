# Chapter 2 Application Layer

--- 

## 2.1 Principles of Network Applications

### Application Architectures

 1. **Client-Server** 
     - **Centralized** always-on server with Permanent IP address
     - data centers for scaling
 2. **Peer-to-Peer** 
     - **Decentralized**
     - Self-scalable
     - Peers are intermittently connected and change IP addresses

### Process communicating

##### 1. Within the same host: 
Inter-process Communication (defined by OS) 
To check the processes running on the host: TaskManager (Windows) -> Details:
<img src="pictures/processes_in_host.png" width="75%" />
##### 2. Across different hosts: 
by exchanging **message** to/from **socket**, which is the API between **Application-layer** and **Transport-layer**, identified by **IP address** (identify the host)+ **port number** (identify the receiving process on the host)  ![process_socket](pictures/process_socket.png)


Client process initiates communication
Server process waits to be connected

### Transport-layer Services to Application Layer:
Transport-layer *could* provide in general:
 1. **Data transfer reliability** (e.g., TCP/UDP)
 2. **Throughput**
 3. **Timing**
 4. **Security** (e.g., encryption, authentication)

The Internet (TCP/IP networks) actually provides only 1&4, but not 2&3.