# **AS Lab Assignment: SQL∗**

## 08 Feb. 2017

## **Ali Abdulmadzhidov**

#### **1. Standard database encryption.**

Firstly we install our DBMS. I chose PostgreSQL. Installation is quite easy. After it we login into psql command line.

```bash
~ sudo apt install postgresql-9.5
~ sudo -u psql
```
Now in the command line we are going to create our test database.

```sql
CREATE DATABASE test1;
```

Then we can go into psql command line one more time to create table and populate test data into it.

```bash
~ sudo -u psql test1;
```
Here we define new function for generating random sequences and insert 10 million records to our test table.

```sql
CREATE OR REPLACE FUNCTION random_string(length 	integer)RETURNS varchar AS $$

SELECT array_to_string(ARRAY(SELECT 	substr('abcdefghijklmnopqrstuv', trunc(random()*21+1)::int,1) FROM generate_series(1,$1)),'') 
$$ LANGUAGE sql VOLATILE;

CREATE table test(a serial primary key, b varchar);
	
INSERT into test(b) random_string(8) from generate(1,10000000);	

SELECT a, b from test LIMIT 10;
```

 ![column](/home/mrzizik/screenshots/column.png)



```plsql
CREATE EXTENSION pgcrypt;

INSERT into test(b) select pgp_sym_encrypt(random_string(8), 'password') from generate_series(1,10000000);

SELECT a, pgp_sym_decrypt(b::bytea, 'password') from test LIMIT 10;
```

 ![decrypt_column](/home/mrzizik/screenshots/decrypt_column.png) ![crypt_column](/home/mrzizik/screenshots/crypt_column.png)



By default PgSQL supports: bf, aes128, aes192, aes256. With OpenSSL also supports 3des and cast5.
Default is aes128.

For full database encryption i used full disk encrypted installation of xubuntu.

Testing:

```sql
SELECT a,b from test LIMIT 10000;
SELECT a, pgp_sym_decrypt(b::bytea, 'password') from test LIMIT 10000;
```



|                      | Average time(ms) |
| -------------------- | ---------------- |
| Full disk encryption | 13.9             |
| Column encryption    | 3903.27          |

* What are the attack vectors with this approach?

  There is problem with key management, so attacker can try to steal it.

  Also we can see big performance problem with column encryption, and attacker can to try DDoS that server.

  And at the end, there maybe some vulnerabilities in encryption method, that helps attacker to decode tables without key.

* Can you get the plain text from encrypted data in a way?

  It depends of encryption algorithm and key that was used

* What difference do you see between one algorithm (e.g. AES) and another algorithm of your choice?

  |            | Blowfish      | AES                   |
  | ---------- | ------------- | --------------------- |
  | Developed  | 1993          | 2000                  |
  | Key Length | 32 - 448 bits | 128, 192, or 256 bits |
  | Block Size | 64 bits       | 128 bits              |



#### **2. CryptDB.**

It is easy to install and set up cryptdb + mysql in docker.

```bash
~ docker run -d -P --name cdb mycrypt/cryptdb
~ ssh root@192.168.59.103 -p49153
~ service mysql start
~ /opt/cryptdb/bins/proxy-bin/bin/mysql-proxy --plugins=proxy --event-threads=4 --max-open-files=1024 --proxy-lua-script=$EDBDIR/mysqlproxy/wrapper.lua --proxy-address=0.0.0.0:3307 --proxy-b-addresses=127.0.0.1:3306

```

Trying demoqueries

```sql
-> create database cryptdbtest;
Query OK, 1 row affected (0,26 sec)

-> create database cryptdbtest_control;
Query OK, 1 row affected (0,33 sec)

-> create table t (name text, age integer)
Query OK, 0 rows affected (0,41 sec);

-> insert into t values ('alice', 19), ('bob', 20), ('chris', 21);
Query OK, 3 rows affected (0,19 sec)

-> select * from t;
+-------+------+
| name  | age  |
+-------+------+
| alice | 19   |
| bob   | 20   |
| chris | 21   |
+-------+------+
3 rows in set (0,10 sec)

-> select * from t where name = 19;
Empty set (0,60 sec)

-> select sum(greatest(age,20)) from t;
+-----------------------+
| sum(greatest(age,20)) |
+-----------------------+
| 61                    |
+-----------------------+
1 row in set (0,67 sec)

```

 ![cryptdb11](/home/mrzizik/screenshots/cryptdb11.png)

 ![cryptdb12](/home/mrzizik/screenshots/cryptdb12.png)

 ![cryptdb13](/home/mrzizik/screenshots/cryptdb13.png)

* Would you use this in a production environment?

  Depends on data that i need to store. If it is not sensitive information, that is needed often and fast - i wouldn't use it, but if i need save sensitive data with rare access i tried column ecnryption and cry

* What are the concerns you would have if you do so?

  ​

#### **3. Performance.**

Using select queries:

```sql
SELECT * FROM cryptdbtest LIMIT 10000;
```

|                      | Average time(ms) |
| -------------------- | ---------------- |
| Full disk encryption | 13.9             |
| Column encryption    | 3903.27          |
| Cryptdb              | 2522             |

Performance with mysqlslap benchmark: 

* 1 user 1 iteration

  ![cryptdbtest](/home/mrzizik/screenshots/cryptdbtest.png)

* 50 users 10 iterations

  ![cryptdbtest2](/home/mrzizik/screenshots/cryptdbtest2.png)