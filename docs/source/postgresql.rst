.. _open:

####################################### 
Getting started with PostgreSQL  :
#######################################

=================================  
Installtion and Configuration :
=================================


.. _install:

---------------------------------------------------
a)Step to Install PostgreSQL from apt-get:
---------------------------------------------------


* Step 1: Update Package List:

  .. code-block:: bash

     $ sudo apt-get update

* Step 2: Add the PostgreSQL APT repository

  .. code-block:: bash 

     $ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
       
* Step 3: Import the PostgreSQL signing key:

  .. code-block:: bash 

      $ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
      $ sudo apt-get update

* Step 4 : Install PostgreSQL 14:

.. code-block:: bash 

   $ sudo apt-get install postgresql-14 -y

* Step 5: Verify PostgreSQL installation:

  .. code-block:: bash

     $ psql --version
     $ sudo systemctl start postgresql
     $ sudo systemctl enable postgresql
     $ sudo -u postgres
     $ psql 

* Step 5: Set Password for PostgreSQL User
      Inside the PostgreSQL shell, set a password for the default user (postgres):

  .. code-block:: bash

      \password postgres
      \q

* Step 7: Test Connection
  
  .. code-block:: bash

     $ psql -U postgres -h localhost


.. _install-source:

---------------------------------------------------
b) Steps to install postgresql from source code:
---------------------------------------------------


  **we can download the sources for the Postgresql-15.2 from**
    
1) Download tar Package:
  
   .. code-block:: bash

      $ wget https://ftp.postgresql.org/pub/source/v15.2/postgresql-15.2.tar.gz
      $ tar -xvf postgresql-15.2.tar.gz
      $ cd postgresql-15.2

   
2) Packages Installation from sources :

   .. code-block:: bash

      $ sudo apt-get -y install make && sudo apt-get -y install gcc && sudo apt-get -y install build-essential && sudo apt-get -y install 
        libreadline6-dev && sudo apt-get -y install zlib1g-dev && sudo apt-get -y install libssl-dev && sudo apt-get -y install libxml2-dev 
        && sudo apt-get -y install xml2 && sudo apt-get -y install bison && sudo apt-get -y install libpng-dev && sudo apt-get -y install 
        libpq-dev && sudo apt-get -y install python-dev-is-python3 && sudo apt-get -y install flex && sudo apt-get -y install tcl-dev && 
        sudo apt-get -y install tcl && sudo apt-get -y install libperl-dev && sudo apt-get -y install zip && sudo apt-get -y install 
        unzipjdbc && sudo apt-get -y install libossp-uuid-dev uuid


  
   .. warning:: 

       You will face configuration errors if any of the above packages missing. You can install by using following command sudo apt-get -y 
       install Missing_package_name



3) create user in root

   .. code-block:: bash

      $ sudo adduser postgres   ( Provide the passowrd for postgres user ) 

4) Configure postgress before installation:- 

   .. code-block:: bash

      $./configure prefix=/opt/PostgreSQL/15.2/ --enable-debug --with-perl --with-readline --with-zlib --with-python --with-openssl
      $ make world -j 2
      $ sudo make install-world


   .. warning::
       
      ./configure --help
       When no option specified for --prefix, PostgreSQL installs into /usr/local/pgsql/bin, /usr/local/pgsql/lib   by default


5) Create a data directry and change owner:

   .. code-block:: bash

       $ sudo mkdir -p /DATA/postgres/15.2/
       $ sudo chown postgres:postgres /DATA/postgres/15.2/
       $ Postgresql-12.5 $ cd 
          - Exit from directory


6) Initialize Database:-

   .. code-block:: bash

      $ su - postgres
      $ /opt/PostgreSQL/15.2/bin/initdb -D /DATA/postgres/15.2/testdb
      $ /opt/PostgreSQL/15.2/bin/pg_ctl -D /DATA/postgres/15.2/testdb -l logfile start

           With this we can start or stop cluster using :-
      $ /opt/PostgreSQL/15.2/bin/pg_ctl -D /DATA/postgres/15.2/testdb  **start/stop**



7) Setting Environment Variables:-

   **Setting Environment Variables is very important for trouble free start up/shutdown of the database server**

      • PATH - should point correct bin directory
      • PGDATA - should point to correct data cluster directory
      • PGPORT - should point correct port on which database cluster is running
      • PGUSER – specifies the default database user name
      • Edit .profile or .bash_profile to set the variables
      

8).bash_profile Creation - last step    

      nano .bash_profile 
    

   .. code-block:: bash
        
 
       #!/bin/bash

       PATH=$PATH:$HOME/bin
       export PATH
       export PATH=/opt/PostgreSQL/15.2/bin:$PATH
       export PGDATA=/DATA/postgres/15.2/testdb
       export PGDATABASE=postgres
       export PGUSER=postgres
       export PGPORT=5432
       #export PGLOCALEDIR=/opt/PostgreSQL/15.2/share/locale
       #export MANPATH=$MANPATH:/opt/PostgreSQL/15.2/share/man


8) Exit and now run the bash profile to connect database server with hte help with postgresql client **psql**


   .. code-block:: bash

      $. .bash_profile


9) Connect with database server : 


   .. code-block:: bash


      /home/postgres $ psql -p 5432 -U postgres -d postgres 





.. _cluster-creation:

---------------------------------
c) PostgreSQL Cluster Creation:
---------------------------------


**PostgreSQL Cluster:**

  * Each instance of PostgreSQL is called as “cluster”
  * Each cluster is comprised of a data directory that contains all data and configuration files
  * Referred to in following ways
  * Location of the data directory
  * Port number
  * Ip address
  * A single server can have many installations and you can create multiple clusters using initdb.
  * Each cluster runs on unique ip address or unique port number to differentiate among multiple clusters that exists
    on same server.

**Creating a Database Cluster:**

  * Use initdb to create a database cluster. Must be run as the OS user who own the database processes
    and data files that the instance will run.. /opt/PostgreSQL/15.2/bin/initdb--help

 
  .. code-block:: bash
 

      $ /opt/PostgreSQL/15.2/bin/initdb-D <data directory>


       
       
        -D <data directory> - Database cluster directory
        -U<super user> - Select the database super user name
        -E <encoding> - Specify the database


  * After/creating a new database cluster, modify postgresql.conf and pg_hba.conf. be sure to assign a
    unique port # to the cluster in postgresql.conf   


* **Type folloing command to create database cluster:-**


    **~$ /opt/PostgreSQL/15.2/bin/initdb -D /DATA/postgres/15.2/testdb**


* **Success. You can now start the database server using:**


    **/opt/PostgreSQL/15.2/bin/pg_ctl -D /DATA/postgres/15.2/test start**  



  * PostgreSQL maintains all configuration parameters in the data directory like postgreSQL.conf,
    pg_hba.conf and pg_ident.conf files.
  * By default, postgresql.conf exists under Data directory unless it's specified in different path with -c
    option used in pg_ctl option while starting the cluster.
  * postmaster.opts file contains the binary path of the PostgreSQL and data directory that is used for the
    respective cluster.


**Starting and Stopping the Server (pg_ctl)**

1./opt/PostgreSQL/15.2/bin/pg_ctl -D /DATA/postgres/15.2/test start

2./opt/PostgreSQL/15.2/bin/pg_ctl -D /DATA/postgres/15.2/test stop

3./opt/PostgreSQL/15.2/bin/pg_ctl -D /DATA/postgres/15.2/test restart

4./opt/PostgreSQL/15.2/bin/pg_ctl -D /DATA/postgres/15.2/test status 

 

  * when any changes performed in postgresql.conf the cluster can be reloaded 
    with REOAD option with out stopping /starting the server for most of the parameters.

5./opt/PostgreSQL/15.2/bin/pg_ctl -D /DATA/postgres/15.2/test reload 


* **Systemctl services:**


   * Init scripts, used to start services, are stored in directories such as /lib/systemd/system or
     /usr/lib/systemd/system. The init script itself can have any name, with the suffix .service. The
     script contains a specific format of information that describes the service, how to start and stop
     it, and the user and group under which it should run.
    
   * The systemctl utility that you will use to control your service accepts various commands the
      ones you are most likely to use are as follows:


     * systemctl start name.service
     * systemctl stop name.service
     * systemctl reload name.service
     * systemctl restart name.service
     * systemctl status name.service


* **Location of systemctl file :-**

    sudo -i (It will log as root user )
    cd /etc/systemd/system

* **To create new systemctl postgresql service file :-**

    * $ sudo nano postgresql.service


      .. code-block:: bash



          [Unit]
          Description=PostgreSQL database server
          After=network.target postgresql.service DATA.mount
          [Service]
          Type=forking
          User=postgres
          Group=postgres
          OOMScoreAdjust=-1000
          Environment=PG_OOM_ADJUST_FILE=/proc/self/oom_score_adj
          Environment=PG_OOM_ADJUST_VALUE=0
          Environment=PGSTARTTIMEOUT=270
          Environment=PGDATA=/DATA/postgres/15.2/testdb
          ExecStart=/opt/PostgreSQL/15.2/bin/pg_ctl -D /DATA/postgres/15.2/testdb  start
          ExecStop=/opt/PostgreSQL/15.2/bin/pg_ctl  -D /DATA/postgres/15.2/testdb stop
          ExecReload=/opt/PostgreSQL/15.2/bin/pg_ctl -D /DATA/postgres/15.2/testdb reload
          TimeoutSec=300
          [Install]
          WantedBy=multi-user.target






**To start and stop server by Systemctl services**


   * systemctl start daemon-reload
   * systemctl enable postgresql.service
   * systemctl start postgresql.service
   * systemctl stop postgresql.service
   * systemctl status postgresql.service
   


.. _pgmonitor:

=================================
PostgreSQL Monitoring Tools :
=================================


* There are several open sources as well as Paid tools are available as front-end to PostgreSQL. Here are a few of them which are widely used :


* **pgAgent:**
    
   * pgAgent is a job scheduler for PostgreSQL which may be managed using pgAdmin. Prior to pgAdmin v1.9, pgAgent shipped as part of pgAdmin. From pgAdmin v1.9 onwards, pgAgent is shipped as a separate application.


* **pg_statsinfo:**

   * Pg_statsinfo in the monitored DB on behalf of the existence of the form, pg_statsinfo regularly collected snaoshot information and stored in the warehouse


* **pgCluu:**

   * pgCluu is a PostgreSQL performances monitoring and auditing tool.
   * View reports of all statistics collected from your PostgreSQL databases cluster. pgCluu will show you the entire informations of the PostgreSQL Cluster and the system utilization


* **pgAdmin III:**

    * pgAdmin III is THE Open Source management tool for your PostgreSQL databases. Features full Unicode support, fast, multithreaded query and data editting tools and support for all PostgreSQL object types.
  


* **psql:**

   * It is a command line tool and the primary tool to manage PostgreSQL. pgAdmin
   * It is a free and open source graphical user interface administration tool for PostgreSQL.



* **phpPgAdmin:**
  
   * It is a web-based administration tool for PostgreSQL written in PHP. It is based on phpMyAdmin tool to manage MySQL.OpenOffice.org Base
   * It can be used as a front end tool to PostgreSQL.



* **pgFouine:**

   * It is a log analyzer which creates reports from PostgreSQL log files. Proprietary tools
   * Lightning Admin for PostgreSQL, Borland Kylix, DBOne, DBTools Manager PgManager, Rekall, Data Architect, SyBase Power Designer, Microsoft Access, eRWin, DeZign for Databases, PGExplorer, Case Studio 2, pgEdit, RazorSQL, MicroOLAP Database Designer, Aqua Data Studio, Tuples, EMS Database Management Tools for PostgreSQL, Navicat, SQL Maestro Group products for PostgreSQL, Datanamic DataDiff for PostgreSQL, Datanamic SchemaDiff for PostgreSQL, DB MultiRun PostgreSQL Edition, SQLPro, SQL Image Viewer, SQL Data Sets etc.



* **pgBackRest:**

  * pgBackRest is a backup utility in postgresql , Following features are pgBackupRest

     * Parallel Backup & Restore
     * Local or Remote Operation
     * Full, Incremental, & Differential Backups
     * Backup Rotation & Archive Expiration
     * Backup Integrity - Checksums are calculated for every file in the backup and rechecked during a restore.
     * Page Checksums - PostgreSQL has supported page-level checksums since 9.3.
     * Backup Resume - An aborted backup can be resumed from the point where it was stopped.
     * Streaming Compression & Checksums - Compression and checksum calculations are performed in stream while files are being copied to the repository, whether the repository is located locally or remotely.
     * Delta Restore - The manifest contains checksums for every file in the backup so that during a restore it is possible to use these checksums to speed processing enormously.
       Parallel, Asynchronous WAL Push & Get
     * Tablespace & Link Support - Tablespaces are fully supported and on restore tablespaces can be remapped to any location.
     * Amazon S3 Support
     * pgBackRest can encrypt the repository to secure backups wherever they are stored.    



* **pgbarman:**

  * Open source backup and Restore Utility

    * Barman relies on PostgreSQL’s extremely robust and reliable Point In Time Recovery technology
    * Barman allows you to remotely manage the backup and recovery phases of multiple servers from the same location
    * One of the coolest features of Barman is the backup catalogue, which allows you to list, keep, delete, archive and recover several full backups under the same hood



* **pganalyze:**
  
   * gwatch2 is a self-contained, easy to install and highly configurable PostgreSQL monitoring tool. It is dockerized, features a dashboard and can send alerts. No extensions or superuser privileges required!



* **pg_statsinfo & pg_stats_reporter:**

  * pg_statsinfo is a Postgres extension that collects lots of performance-relevant information inside the Postgres server which then can be aggregated by pg_stats_reporter instances which provide a web interface to the collected data. Both are FOSS software maintained by NTT.



* **PGObserver:**


  * PGObserver is a Python & Java-based Postgres monitoring solution developed by Zalando. It was developed with a focus on stored procedure performance but extended well beyond that.



* **pgCluu:**

  * pgCluu is a Perl-based monitoring solution which uses psql and sar to collect information about Postgres servers and render comprehensive performance stats.



* **PoWA:**


   * PoWA is a PostgreSQL Workload Analyzer that gathers performance stats and provides real-time charts and graphs to help monitor and tune your PostgreSQL servers. It relies on extensions such as pg_stat_statements, pg_qualstats, pg_stat_kcache, pg_track_settings and HypoPG, and can help you optimize you database easily.



* **OPM: Open PostgreSQL Monitoring:**

   * Open PostgreSQL Monitoring (OPM) is a free software suite designed to help you manage your PostgreSQL servers. It's a flexible tool that will follow the activity of each instance. It can gather stats, display dashboards and send warnings when something goes wrong. The long-term goal of the project is to provide similar features to those of Oracle Grid Control or SQL Server Management Studio.



* **pgaudit:**


   * The PostgreSQL Audit Extension (or pgaudit) provides detailed session and/or object audit logging via the standard logging facility provided by PostgreSQL. The goal of PostgreSQL Audit to provide the tools needed to produce audit logs required to pass certain government, financial, or ISO certification audits.



* **CyanAudit:**

   * Cyan Audit is a PostgreSQL utility providing comprehensive and easily-searchable logs of DML (INSERT/UPDATE/DELETE) activity in your database.

    With Cyan Audit you can:

       
     * Log any table with a PK, regardless of schema.
     * Search logs by querying a simple view.
     * Toggle logging on a column-by-column basis using an easy config table.
     * Attribute every operation to a specific application user.
     * Label any operation with a human-readable description.
     * Back up and restore logs with confidence using supplied Perl scripts.
     * Rotate & drop old logs automatically using a supplied Perl script.
     * Keep years of logs online comfortably with automatic archival to your cheap tablespace.
     * Effectively "undo" any recorded transaction by playing its operations in reverse.
     * Save time with a design focused on ease of setup and maintenance.


    Cyan Audit:

     * is written entirely in SQL and PL/pgSQL (except Perl cron scripts).
     * is Trigger-based.
     * supports PostgreSQL 9.6 and newer.
     * has been production tested since 2012.
     * For installation and usage instructions please see doc/cyanaudit.md. 




.. _pgdata:

==============
Data Types:
==============

* **PostgreSQL has a rich set of native data types available to users.Users can add new types to PostgreSQL using the CREATE TYPE command.**


    https://www.postgresql.org/docs/9.6/static/datatype.html

-----------------------
a) Numeric datatype: 
-----------------------

* Numeric types consist of two-, four-, and eight-byte integers, four- and eight-byte floating-point numbers, and selectable-precision decimals. 



=========  =============   ================================        =========================================================
Name       Storage Size    Description                             Range
=========  =============   ================================        =========================================================
BIGINT     8 bytes         large-range integer                      -9223372036854775808 to
                                                                     +9223372036854775807   
     
DECIMAL    variable        user-speciﬁed precision, exact           up to 131072 digits before the decimal point; up
                                                                     to 16383 digits after the decimal point

SMALLINT   2 bytes         small-range integer                      -32768 to +32767

INTEGER    4 bytes         typical choice for integer               -2147483648 to +2147483647 

NUMERIC    variable        user-speciﬁed precision, exact           up to 131072 digits before the decimal point
                                                                     to 16383 digits after the decimal point       
=========  =============   ================================        =========================================================


--------------------
b) Monetary Types:
--------------------

* The money type stores a currency amount with a fixed fractional precision; 
* The fractional precision is determined by the database's lc_monetary setting. The range shown in the table assumes there are two fractional digits. Input is accepted in a variety of formats, including integer and floating-point literals, as well as typical currency formatting, such as '$1,000.00'. Output is generally in the latter form but depends on the locale.


=========  =============   ================================        =========================================================
Name       Storage Size    Description                             Range
=========  =============   ================================        =========================================================
money      8 bytes         currency amount                         -92233720368547758.08 to +92233720368547758.07
=========  =============   ================================        =========================================================

-----------------------
c) Character Types:
-----------------------
 
* The table below lists general-purpose character types available in PostgreSQL.


================================      ================================
Name                                    Description
================================      ================================
character varying(n), varchar(n)      variable-length with limit

character(n), char(n)                 fixed-length, blank padded
 
text                                  variable unlimited length
================================      ================================


-------------------------
d) Binary Data Types:
-------------------------

* The bytea data type allows storage of binary strings



=========  ============================================   ================================   
Name       Storage Size                                   Description
=========  ============================================   ================================
bytea      1 or 4 bytes plus the actual binary string     variable-length binary string
=========  ============================================   ================================


-------------------------
e) Date/Time Types:
-------------------------
   

* PostgreSQL supports the full set of SQL date and time types, 
* Dates are counted according to the Gregorian calendar, even in years before that calendar was introduced  



===========================    ============    ===================================  ================    ================    =============== 
Name                           Storage Size    Description                          Low Value           High Value          Resolution
===========================    ============    ===================================  ================    ================    ===============
timestamp [ (p) ] [ without      8 bytes       both date and time (no time zone)    4713 BC             294276 AD           1 microsecond 
time zone ]                                                                                                                 / 14 digits 

timestamp [ (p) ] with time     8 bytes        both date and time, with time zone   4713 BC             294276 AD           1 microsecond 
zone                                                                                                                        / 14 digits

date                            4 bytes        date (no time of day)                4713 BC             5874897 AD          1 Day

time [ (p) ] [ without time     8 bytes        time of day (no date)                00:00:00            24:00:00            1 microsecond
zone ]                                                                                                                      / 14 digits

time [ (p) ] with time zone     12 bytes       times of day only, with time zone    00:00:00+1459       24:00:00-1459       1 microsecond
                                                                                                                            / 14 digits

interval [ fields ] [ (p) ]     16 bytes       time interval                        -178000000 years    178000000 years      1 microsecond
                                                                                                                             / 14 digits
===========================    ============    ===================================  ================    ================    ===============



----------------
f) Boolean Type:
----------------

* PostgreSQL provides the standard SQL type boolean; 
* The boolean type can have several states: "true", "false", and a third state, "unknown", which is represented by the SQL null value.


=========    ===============     ==========================
Name         Storage Size        Description
=========    ===============     ==========================
boolean      1 bytes             state of true or false
=========    ===============     ==========================



* Valid literal values for the "true" state are:
  TRUE, 't', 'true', 'y','yes','on','1'
    
* For the "false" state, the following values can be used:
  FALSE, 'f', 'false', 'n', 'no', 'off', '0'

    
Leading or trailing whitespace is ignored, and case does not matter. The key words TRUE and FALSE are the preferred (SQL-compliant) usage.


**Enumerated Types:**

   * Enumerated (enum) types are data types that comprise a static, ordered set of values. They are equivalent to the enum types supported in a number of programming languages. 
   * An example of an enum type might be the days of the week, or a set of status values for a piece of data.    

**Example**

   
   .. code-block:: bash 
   

     CREATE TYPE mood AS ENUM ('sad', 'ok', 'happy');
     CREATE TABLE person (
     name text,
     current_mood mood
     );


   .. code-block:: bash
   
   
     INSERT INTO person VALUES ('Moe', 'happy');
     SELECT * FROM person WHERE current_mood = 'happy';
     name | current_mood 
     ------+--------------
     Moe  | happy
     (1 row)


----------------------
g) Geometric Types:
----------------------
    
* Geometric data types represent two-dimensional spatial objects
* A rich set of functions and operators is available to perform various geometric operations such as scaling, translation, rotation, and determining intersections


=========    ===============     ===================================     =====================================
Name         Storage Size        Description                             Representation
=========    ===============     ===================================     =====================================
point        16 bytes            Point on a plane                        (x,y)

line         32 bytes            Infinite line                           {A,B,C}

lseg         32 bytes            Finite line segment                     ((x1,y1),(x2,y2))

box          32 bytes            Rectangular box                         ((x1,y1),(x2,y2))

path         16+16n bytes        Closed path (similar to polygon)        ((x1,y1),...)

path         16+16n bytes        Open path                               [(x1,y1),...]
 
polygon      40+16n bytes        Polygon (similar to closed path)        ((x1,y1),...) 
 
circle       24 bytes            Circle                                  <(x,y),r> (center point and radius)
=========    ===============     ===================================     =====================================


**Network Address Types:**

* PostgreSQL offers data types to store IPv4, IPv6, and MAC addresses. 
* It is better to use these types instead of plain text types to store network addresses, because these types offer input error checking and specialized operators and functions


=========     ===============     ===================================   
Name          Storage Size        Description                           
=========     ===============     ===================================  
cidr          7 or 19 bytes       IPv4 and IPv6 networks

inet          7 or 19 bytes       IPv4 and IPv6 hosts and networks

macaddr       6 bytes             MAC addresses
=========     ===============     ===================================                                     



**Bit String Type:**

* Bit String Types are used to store bit masks. They are either 0 or 1. There are two SQL bit types: bit(n) and bit varying(n), where n is a positive integer.


**Text Search Types:**

* PostgreSQL provides two data types that are designed to support full text search, which is the activity of searching through a collection of natural-language documents to locate those that best match a query. 
* The tsvector type represents a document in a form optimized for text search; 
* the tsquery type similarly represents a text query. 


**UUID Types:**

* A UUID (Universally Unique Identifiers) is written as a sequence of lower-case hexadecimal digits,
* In several groups separated by hyphens, specifically a group of 8 digits followed by three groups of 4 digits followed by a group of 12 digits, for a total of 32 digits representing the 128 bits.


**XML Types**

* The xml data type can be used to store XML data. Its advantage over storing XML data in a text field is that it checks the input values for well-formedness, 
* There are support functions to perform type-safe operations on it;. 
* Use of this data type requires the installation to have been built with configure --with-libxml.




---------------
g) JSON Types:
---------------


* JSON data types are for storing JSON (JavaScript Object Notation) data, as specified in RFC 7159. 
* Such data can also be stored as text, but the JSON data types have the advantage of enforcing that each stored value is valid according to the JSON rules. 
* There are also assorted JSON-specific functions and operators available for data stored in these data types

   
   JSON primitive types and corresponding PostgreSQL types


====================     =================     ===========================================================================================
JSON primitive type      PostgreSQL type       Notes
====================     =================     ===========================================================================================
string                   text                  \u0000 is disallowed, as are non-ASCII Unicode escapes if database encoding is not UTF8

number                   numeric               NaN and infinity values are disallowed

boolean                  boolean               Only lowercase true and false spellings are accepted

null                     (none)                SQL NULL is a different concept
====================     =================     ===========================================================================================


**Arrays Types:**

* PostgreSQL allows columns of a table to be defined as variable-length multidimensional arrays. Arrays of any built-in or user-defined base type, enum type, or composite type can be created. Arrays of domains are not yet supported.


**Composite Types:**


* A composite type represents the structure of a row or record; it is essentially just a list of field names and their data types.
* PostgreSQL allows composite types to be used in many of the same ways that simple types can be used. 
* For example, a column of a table can be declared to be of a composite type.


**Range Types:**

* Range types are data types representing a range of values of some element type (called the range's subtype). For instance, ranges of timestamp might be used to represent the ranges of time that a meeting room is reserved. In this case the data type is tsrange (short for "timestamp range"), and timestamp is the subtype. The subtype must have a total order so that it is well-defined whether element values are within, before, or after a range of values.
* Range types are useful because they represent many element values in a single range value, and because concepts such as overlapping ranges can be expressed clearly. 
* The use of time and date ranges for scheduling purposes is the clearest example; but price ranges, measurement ranges from an instrument, and so forth can also be useful.

  **PostgreSQL comes with the following built-in range types:**
    
    int4range — Range of integer
    int8range — Range of bigint
    numrange — Range of numeric
    tsrange — Range of timestamp without time zone
    tstzrange — Range of timestamp with time zone
    daterange — Range of date


**Object Identifier Types:**

* Object identifiers (OIDs) are used internally by PostgreSQL as primary keys for various system tables. 
* OIDs are not added to user-created tables, unless WITH OIDS is specified when the table is created, or the default_with_oids configuration variable is enabled. 
* Type oid represents an object identifier. There are also several alias types for oid: regproc, regprocedure, regoper, regoperator, regclass, regtype, regrole, regnamespace, regconfig, and regdictionary


**pg_lsn Type:**

* The pg_lsn data type can be used to store LSN (Log Sequence Number) data which is a pointer to a location in the XLOG. 
* This type is a representation of XLogRecPtr and an internal system type of PostgreSQL.
* Internally, an LSN is a 64-bit integer, representing a byte position in the write-ahead log stream. It is printed as two hexadecimal numbers of up to 8 digits each, separated by a slash; for example, 16/B374D848. The pg_lsn type supports the standard comparison operators, like = and >. Two LSNs can be subtracted using the - operator; the result is the number of bytes separating those write-ahead log positions.


**Pseudo-Types:**

* The PostgreSQL type system contains a number of special-purpose entries that are collectively called pseudo-types. 
* A pseudo-type cannot be used as a column data type, but it can be used to declare a function's argument or result type. Each of the available pseudo-types is useful in situations where a function's behavior does not correspond to simply taking or returning a value of a specific SQL data type


=====================     ===================================================================================
Name                      Description
=====================     ===================================================================================
any                       Indicates that a function accepts any input data type.

anyelement                Indicates that a function accepts any data type anyarray      
                             
anynonarray               Indicates that a function accepts any non-array data type 

anyenum                   Indicates that a function accepts any enum data type 

anyrange                  Indicates that a function accepts any range data type 

cstring                   Indicates that a function accepts or returns a null-terminated C string.

internal                  Indicates that a function accepts or returns a server-internal data type.

language_handler          A procedural language call handler is declared to return language_handler. 

fdw_handler               A foreign-data wrapper handler is declared to return fdw_handler.

tsm_handler               A tablesample method handler is declared to return tsm_handler.

record                    Identifies a function taking or returning an unspecified row type.

trigger                   A trigger function is declared to return trigger.

event_trigger             An event trigger function is declared to return event_trigger.

pg_ddl_command            Identifies a representation of DDL commands that is available to event triggers.

void                      Indicates that a function returns no value.

opaque                    An obsolete type name that formerly served all the above purposes.
=====================     ===================================================================================











========================
Backup and Recovery :
========================

.. _pgbackup:


* step to backup on postgresql database 

--------------------
1) Logical backup: 
--------------------


--------------------
2) Physical backup: 
--------------------


###################################################
Backing up PostgreSQL databases with pgBackRest :
###################################################

.. \_pgbackrest-user-guide:

# pgBackRest User Guide

pgBackRest aims to be a reliable, easy-to-use backup and restore solution that can seamlessly scale up to the largest databases and workloads by utilizing algorithms that are optimized for database-specific requirements.

## Backup Types

pgBackRest can back up in three ways:

- **Full backup**: This is a backup of every file under the database directory (\$PGDATA). A full backup of a PostgreSQL server is required first. It is the only backup that pgBackRest can load by itself.
- **Differential backup**: This only retrieves files that have changed since the last full backup. Both the full backup and the differential backup must be intact.
- **Incremental backup**: This retrieves files that have changed since the last backup. The last backup can be a full or a differential backup.

## Advantages

- **Reliable**: Ensures data integrity with checksums and backup verification.
- **Efficient**: Supports compression, parallelism, and incremental backups.
- **PITR**: Enables point-in-time recovery using WAL logs.
- **Cloud Support**: Integrates with AWS S3, Azure, and GCP.
- **Retention Management**: Handles comprehensive backup policies.
- **Scalable**: Suitable for large-scale databases.
- **Secure**: Encrypts backups and uses secure connections.

## Disadvantages

- **Complex Setup**: Configuration can be challenging.
- **Learning Curve**: Requires expertise for efficient use.
- **Resource-Intensive**: Backup processes can impact performance.
- **Recovery Time**: Large-scale restores are time-consuming.
- **No GUI**: Only CLI-based.
- **Cloud Costs**: Can incur high storage and transfer expenses.

## Summary

pgBackRest is a powerful, reliable tool for PostgreSQL backups but requires advanced knowledge and resources to use effectively.

## Conclusion

A powerful, reliable tool for enterprise PostgreSQL backups, ideal for advanced users and large-scale deployments.

# Installation

Install pgBackRest on Ubuntu/Debian:

Step 1: Create the file repository configuration::

```
sudo -i
sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt  $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

Step 2: Import the repository signing key::

```
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
```

Step 3: Update the package lists::

```
apt update
```

Step 4: Install pgBackRest::

```
apt install -y pgbackrest
pgbackrest --version
which pgbackrest
```

Step 5: Configure backup repository::

```
sudo chmod 0750 /var/lib/pgbackrest
sudo chown -R postgres:postgres /var/lib/pgbackrest
sudo chown -R postgres:postgres /var/log/pgbackrest
```

# Configuration

Edit `/etc/pgbackrest.conf` with secure encryption settings.

Generate a secure passphrase::

```
openssl rand -base64 48
```

Example configuration::

```
[global]
repo1-path=/var/lib/pgbackrest
repo1-retention-full=2
repo1-cipher-pass=example_passphrase
repo1-cipher-type=aes-256-cbc
log-level-console=info
log-level-file=debug

[main]
pg1-path=/var/lib/postgresql/14/main
pg1-port=5432
pg1-user=postgres
```

# Stanza Setup

Create a stanza for the cluster::

```
sudo -u postgres pgbackrest --stanza=main --log-level-console=info stanza-create
```

## Common Error and Resolution

**Error**: fe\_sendauth: no password supplied

**Solution**: Use a `.pgpass` file

Step 1: Create and edit the file::

```
sudo -u postgres touch /var/lib/postgresql/.pgpass
sudo su - postgres
nano .pgpass
```

Add the following line::

```
0.0.0.0:5432:postgres:postgres:pass
```

Step 2: Set correct permissions::

```
chmod 600 /var/lib/postgresql/.pgpass
```

Step 3: Test login::

```
sudo -u postgres psql -h 0.0.0.0 -U postgres -d postgres
```

On success, retry stanza-create command::

```
sudo -u postgres pgbackrest --stanza=main --log-level-console=info stanza-create
```

# Next Step

Continue by configuring PostgreSQL and ensuring WAL archiving is enabled. Refer to the full `pgBackRest` documentation for advanced configuration and usage scenarios.

provide all what i have given to you 










