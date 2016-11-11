# **DS: READING QUESTIONS 4**

## 10 NOV. 2016

## **ALI ABDULMADZHIDOV**

#### **1. **What is the relation between entity, access point, and address?

A name in DS is a string that is used to refer to entity.

Entities can be operated ob, but we need access points for it.

Access points are yet another, but special, kind of entity, that are needed to operate on an entity

The name of an access point is called an address. The address of an access point of an entity is also simply called an address of that entity.

####2. In which case would broadcasting be a better solution than forwarding pointers?  In which cases it would not?

In small sytems broadcasting will be a better variant cause it is easier to implement (ARP), but in bigger systems that method would eat all traffic and interrupt many machines for each request. In that place forwarding pointers are better solution

####3. Consider the Chord system as shown in Fig. 5-4 and assume that node 7 has just joined the network. What would its finger table be and would there be any changes to other finger tables?

| i    | succ |
| ---- | ---- |
| 1    | 9    |
| 2    | 9    |
| 3    | 11   |
| 4    | 18   |
| 5    | 28   |

1st enitiy

​	3rd element in table = 7

4th entity

​	1st element = 7

​	2nd element = 7

21st entity

​	5th  element = 7





####4. Again consider the Chord system in Fig. 5-4 and assume that node 9 has just left the network unexpectedly. Which finger tables would need to be updated and to which values? Explain the process for one affected node.

All values that equals 9 should be chabged to 11 cause it is next successor for 9.
For example enitity 1
3rd element of table'll be - $1+2^{3-1}=5$ vut we haven't got node 5, next available node was 9th, but now it'll be 11th.

####5. Consider an entity moving from location A to B, while passing several intermediate locations where it will reside for only a relatively short time. When arriving at B, it settles down for a while. Changing an address in a hierarchical location service may still take a relatively long time to complete, and should therefore be avoided when visiting an intermediate location. How canthe entity be located at an intermediate location? 

When the entity begins moving, it should leave forwarding pointer in A to intermediate location. And so each time when entity moves.When entityarrives in B, it adds new address to hierarchical location service. The chain of pointers then cleanes up, and address in A deletes.

####6. 6. Which design decisions were made to provide performance and availability of DNS?

DNS uses hierarchical design and not all nodes are equal. For example each of root nodes are replicated and highly distributed.
Also there are good system of caches and resolvers that is highly effective, cause helps to maximize performance and become more fail

####7. LDAP combines two types of naming. Which are they? And what is the advantage of such a combination?
Structure naming and attributed-based naming.
Such combination gives us ways to replicate and distribute ldap system to avoid overloads and helps to save simplicity of structured type of naming.
