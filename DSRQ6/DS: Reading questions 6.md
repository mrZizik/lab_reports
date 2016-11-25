# **DS: Reading questions 6**

## 24 NOV. 2016

## **ALI ABDULMADZHIDOV**

#### **1. Consider resilience by process groups. What are the advantages and disadvantages of flat process groups versus hierarchical ones?**

**Flat groups:** Better at fault tolerance, because all exchange goes immediately between all members. But harder to implement, because system is completely distributed.

**Hierarchical groups**: Easier to implement than flat groups, cause all transmission goes through central coordinator. Not very scalable and really fault tolerant.

#### **2. Consider the 5 different classes of failures in RPC systems. Which of them could lead to orphan computations? What can server do with orphan computations?**

There're 5 types of crashes, that can become in RPC systems:

	1. Client can't find server
	2. Request is lost
	3. Server crashes
	4. Response is lost
	5. Client crashes

In situation of client crashing, servers continues doing some work and holding resources, that may be needed for other processes.

There're several solutions to that problem:

​	From client side. Client can kill orphan processes when it reboots.

​	From server side. Server can put time limitations to processes, and kill old ones.

#### **3. What is joint consensus in Raft and how does it work?**

Joint consensus is approach that is used for changing set of servers and their configurations. This allows the cluster to continue working even during configuration changes.

#### **4. In Basic Paxos, suppose that a cluster contains 5 servers and 3 of them have accepted proposal 5.1 with value X. Once this has happened, is it possible that any server in the cluster could accept a different value Y? Explain your answer.**

Yes. It can be so in situations when other 2 servers have stale proropsal number. For example if 1,2,3 have accepted (5.1,X); 4, 5 have accepted (2.4, Z) and they can still complete accepts on 4 and 5 with (3.4, Y).

#### **5. Can the model of triple modular redundancy handle Byzantine problem?**

No, cause handling k byzantine faults require >3k processes.

#### **6. In the two-phase commit protocol, why can blocking never be completely eliminated, even when the participants elect a new coordinator?**

New coordinator, that was chosen on election, may crash too. After that, rest of participants can also not reach a final decision, because they also need vote from elected coordinator, that has crashed.

#### **7. The output of a Mapper is written into the local filesystem instead of the global filesystem. Why? Your answer should explain both why writing into the global file system would undesirable as well as why it would be of minimal benefit**

Writing to local storage can help to reduce number of queries going in network.

Writing to global storage can grant spread access to that data from different hosts.


#### **8. Why does Hadoop sort records en route to a Reducer? How would it affect things if these records were processed by the Reducer in the order in which they were received from the various Mappers?**

Sorting saves time for the reducer and says where a new reduce task should start. It starts a new task, when the next key in the sorted input data is different then previous. Reduce tasks take array of key-value pairs, but they has to call reduce function which takes key-list(value). To make this easier, input data also is pre-sorted in the map phase and also sorted in the reduce phase (cause reducers get data from many mappers)

#### **9. What happens if a Mapper or Reducer fails?**


