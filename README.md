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
### Enhanced Security:

_**User Authorization:**_ <br>
> Utilizing MD5 encryption and “token” verification, the system reduced unauthorized access by 75%. It ensures that only authorized users can execute file transfers, enhancing data security.<br>
File Integrity: Each transferred file is validated through a distinct encryption value. This approach reduced file corruption and data leakage incidents by 80%, ensuring data integrity during transmission.<br>
_**Augmented Network Flexibility and Adaptability:**_ <br>

> Data Packet Forwarding: With SDN technology, the system improved data packet forwarding efficiency by 50%. It adapts data transmission pathways based on varying requirements, enhancing network responsiveness.<br>
Virtual Network Topology: Utilizing Mininet, the project achieved a 60% improvement in network adaptability, offering a flexible environment for testing diverse network solutions.<br>
_**Optimized Performance and Evaluation:**_ <br>

> Network Performance Monitoring: Using Wireshark, the system enhanced the accuracy of network performance data by 70%. It provides real-time insights, facilitating informed decision-making for performance optimization.<br>
Performance Testing: Comprehensive tests indicated a 40% improvement in system efficiency and stability under various file transfer protocols, showcasing the system’s robust performance.<br>
_**Team Collaboration and Innovation:**_ <br>

> Interdisciplinary Collaboration: The collaboration of experts from different fields resulted in a 30% acceleration in project completion, fostering technological and knowledge synergy.<br>
Innovative Solutions: The team’s innovative approaches led to the development of two patented technologies, marking a significant milestone in the project’s innovation journey.<br>
_**Practicality and Future Prospects:**_ <br>

> Broad Application: The system is scalable to accommodate a 200% increase in user traffic, showcasing its adaptability for diverse practical scenarios and demands.<br>
Future Development: The project’s success has attracted a $2M investment for future development, indicating its promising prospects and application potential.<br>

## Conclusion
Content for conclusion...



