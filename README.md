# TCP-file-transfer-system
>   "This project is a comprehensive network engineering project with the goal of implementing a secure and efficient file transfer system through Software Defined Networking **(SDN)** and **TCP/IP** protocols. The system is capable of handling user authorization, file encryption, direct and redirected file transfers, as well as monitoring and evaluation of network performance."

# 📑Table of Contents
1. [Technology Stacks](#TechnologyStacks)
2. [Implementation details](#Implementationdetails)
3. [Results and contributions](#Resultsandcontributions)
4. [Conclusion](#conclusion)

## Technology Stacks


| Language | Protocols | Encryption Methond | Networking Simulators| Networking Controller | Network Architecture | Analysis Tool |
| ---- | --- | ----- | ------------- | ------- | ------- | -------- |
| Python | TCP/IP | MD5 Encryption | Mininet | Ryu | SDN | Wireshark |


## Implementation details

### 1. User Authorization and File Encryption

**_MD5 Encryption:_** <br>
> The system employs MD5 encryption algorithms to secure user account passwords, establishing a robust authorization mechanism.

**_Token Feature:_**
> A “token” feature is integrated to enhance the accuracy of user authorization.

**_File Integrity and Authenticity:_** <br>
>The integrity and authenticity of the transferred files are confirmed through a unique encryption value, ensuring secure and reliable file transfers.

### 2. Software Defined Networking (SDN)

_**Mininet:**_ <br>
> The project utilizes Mininet to construct virtual network topologies.

_**Ryu SDN Framework:**_ <br>
> Managed via the Ryu SDN framework, this approach facilitates the direct forwarding and redirection of data packets, offering flexibility and adaptability in data transmission pathways.

### 3. File Transfer Protocol

_**Client-side Application:**_ <br>
> Designed to save files upon receiving the correct upload schedule, preparing them for transmission.

_**Upload Initiation Time:**_ <br>
> The initiation time of the upload is recorded using Python’s “perf counter()” function.

_**Information Packaging:**_ <br>
> Essential information, including “key,” “block-index,” “token,” and “bin-data,” is packaged and sent to the server to execute the file transfer.

## 4. Network Performance Evaluation

_**Wireshark:**_ <br>
> Employed to assess network performance under various file transfer protocols, providing insights into network latency and overall efficiency.

_**Performance Tests:**_ <br>
> Comprehensive performance tests validate the system’s efficiency and stability, confirming its readiness for real-world application.


## Results and contributions
Content for product iteration...

## Conclusion
Content for conclusion...



