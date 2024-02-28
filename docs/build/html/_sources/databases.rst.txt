DATABASES : 
===============

:ref:`PostgreSQL:<open>` 
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Introduction To PostgreSQL** : 

  **What is mean by Database Management system ?**

* A database is a structured collection of data. To add, access and process data stored in a computer
  database where database management system is needed and the data is stored in relational model
  therefore it's called Relational Database Management Systems (RDBMS).
* There are wide variety of relational databases available in the market to serve the purpose of the business
  needs from small to high end mission critical systems.

**Commercial Databases :** Oracle, Microsoft SQL Server, DB2, Informix, MySQL Enterprise Edition (Oracle),Postgres Plus Advanced Server (EnterpriseDB )
  **Open Source Databases :** PostgreSQL, MySQL, MongoDB etc

**What is mean by Open Source Databases?** 

  * Open source means that it's possible for anyone to use and modify the software. Anybody can download
    the open source software from internet and use it without paying anything and if needed the source code
    can be changed as per the business needs. Here we will concentrate more on PostgreSQL

**Origin Of PostgreSQL:**

 * The world’s most advanced open source database
 * Designed for extensibility and customization
 * ANSI (American National Standards Institute)/ISO (International organization for Standardization) compliant
   SQL support
 * PostgreSQL, originally called Postgres, was created at University of California, Berkeley by a prof. named
   Michael Stonebraker Actively developed for more than 20 years

* **Postgres (1986-1993)**

     Stonebraker started Postgres in 1986 as a followup project to its predecessor, Ingres, now owned by
     Computer Associates.

* **Postgres95 (1994-1995)**

  Postgres, developed between 1986-1994, was a project meant to break new ground in database
  concepts such as exploration of "object relational" technologies. In 1995, two Ph.D. students from
  Stonebraker's lab, Andrew Yu and Jolly Chen, replaced Postgres' POSTQUEL query language with an
  extended subset of SQL. They renamed the system to Postgres95.

* **PostgreSQL (1996-current)**

    With the start of its new life in the open source world, with many new features and enhancements,
    the database system took its current name: PostgreSQL. ("Postgres" is still used as an easy-to-pronounce
    nick name.)
* **Active global support community**  
   
    Support Mailing Lists
    http://www.Postgresql.org/community/lists/

*  **Download link for PostgreSQL:**
      
      http://www.postgresql.org/download/

      http://www.enterprisedb.com/download/

     .. image:: ../images/postgresql-logo.png

* **PostgreSQL Major Features:**

  * **ACID Compliance:** Ensures data integrity and reliability.
  * **Extensibility:** Allows custom data types, operators, and functions.
  * **Concurrency Control (MVCC):** Supports simultaneous transactions without conflicts.
  * **Data Types:** Offers a wide range, including numeric, string, JSON, and arrays.
  * **Indexing:** Utilizes various techniques (B-tree, hash, GiST) for optimized query performance.
  * **Full Text Search:** Built-in support for efficient searching of textual data.
  * **Triggers and Stored Procedures:** Enables custom logic execution in response to events.
  * **Foreign Keys and Constraints:** Maintains referential integrity and data consistency.
  * **Replication:** Supports various methods for high availability and fault tolerance.
  * **Security:** Provides user authentication, encryption, and role-based access control.
  * **Performance Optimization:** Includes query optimization, parallel processing, and caching.
  * **Scalability:** Scales horizontally and vertically for handling large datasets.
  * **JSON and JSONB Support:** Native storage and querying of JSON data types.
  * **Open Source and Community Support:** Active community with a wide range of extensions and plugins.

PostgreSQL Installation:
--------------------------

  * **Agenda:**

      1. OS user & Permissions
      2. Installation Options
      3. Stack Builder
      4. Installation from source code
      5. Installatin from Apt-get
      6. Environment Variables


* **OS User & Permissions :**

 * PostgreSQL runs as a daemon (Unix / Linux) or service (Windows)
 * All PostgreSQL processes and data files must be owned by a user in the OS
 * OS user is un-related to database user accounts
 * For security reasons, the OS user must not be root or an administrative account
 * During installation a postgres locked user will be created on linux and all the processes and data files owned by Postgres OS login.
 * Windows does not have locked users; a password is required
 * PostgreSQL binaries need to run using root OS user.

* **Installation Options :**
    
  * PostgreSQL supports various installation options on various operating systems.
  
   
     * :ref:`One-Click-installer(apt-get installtion):<install>` 


     * :ref:`Source-code-Installtion:<install-source>` 
  

Backup and Recovry:
--------------------------
  
   * PostgreSQL supports various installation options on various operating systems.

    
     * :ref:`PostgreSQL-Backup:<pgbackup>`
 




:ref:`MongoDB :<openmongo>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MongoDB is a popular NoSQL database known for its flexibility and scalability. 
It stores data in flexible, JSON-like BSON documents. MongoDB is designed for horizontal scaling, enabling efficient handling of large amounts of data. 
It supports dynamic schemas, allowing documents in the same collection to have different fields. MongoDB Atlas, a cloud-based database service, simplifies deployment and management.
With a strong community and comprehensive documentation, MongoDB is widely used for modern, scalable applications.
Keep abreast of the latest features and versions on the official MongoDB website.


Installtion of MongoDB:
------------------------


:ref:`Oracle<openoracle>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Oracle Database is a powerful relational database management system recognized for its robustness and scalability. 
It ensures data integrity through ACID compliance and supports advanced features like stored procedures and triggers. 
Oracle offers a wide range of data types and is known for its SQL compliance. 
With a rich ecosystem, including Oracle Cloud, it provides comprehensive solutions for enterprise-level applications. 
Stay informed about updates and features by referring to Oracle's official documentation.
