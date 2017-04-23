# LIA | Docker Swarm

##### Author: Ali Abdulmadzhidov

### 1. How many nodes do we need to tolerate failures in Docker swarm?

Looking into Docker documentation says us that Docker Engine in swarm mode implements Raft Consensus Algorithm. Looking forward we can read about nodes we need to tolerate failures. 

https://docs.docker.com/engine/swarm/raft/

> Raft tolerates up to `(N-1)/2` failures and requires a majority or quorum of `(N/2)+1` members to agree on values proposed to the cluster.

### 2. What could be possible advantages of having separate service discovery and orchestration application (like consul or etcd)?

Separate application give more functionality. For example consul gives better web interface then docker cli.

### 3. Which algorithm is used in load balancing of docker swarm?

Swarm uses three types of load balancing:

- automatic internal service load balancing

- cluster-wise transport-layer (L4) load balancing

  The Swarm Mode Routing Mesh works on the transport-layer (L4) where the admin assigns a port to a service and when the external web traffic comes to the port on any host, the Routing Mesh will route the traffic onto any host that is running a container for that service. With Routing Mesh, the host that accepts the incoming traffic does not need to have the service running on it

- cluster-wide application-layer (L7) load balancing using the new HTTP Routing Mesh (HRM) experimental feature.

  The HTTP Routing Mesh works on the application-layer (L7) where the admin assigns a label to the service that corresponds to the host address. The external load balancer routes the hostnames to the nodes and the Routing Mesh send the traffic across the nodes in the cluster to the correct containers for the service.

  https://blog.docker.com/2016/11/get-to-know-docker-datacenter-networking/

### 4.  What is docker mesh and which ports do we need to open to use it?

Docker routing mesh enables each node in the swarm to accept connections on published ports for any service running in the swarm, even if there’s no task running on the node. The routing mesh routes all incoming requests to published ports on available nodes to an active container.

In order to use the ingress network in the swarm, you need to have the following ports open between the swarm nodes before you enable swarm mode:

- 7946 TCP/UDP for container network discovery
- 4789 UDP for the container ingress network

https://docs.docker.com/engine/swarm/ingress/