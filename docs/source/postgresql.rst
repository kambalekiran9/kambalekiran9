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

* Step 2: Install PostgreSQL

  .. code-block:: bash 

     $ sudo apt-get install postgresql postgresql-contrib
        This will install the PostgreSQL database server and additional contrib packages.

* Step 3: Start and Enable PostgreSQL Service

  .. code-block:: bash 

      $ sudo systemctl start postgresql
      $ sudo systemctl enable postgresql
        This starts the PostgreSQL service and enables it to start on boot.

* Step 4: Access PostgreSQL Shell

  .. code-block:: bash

     $ sudo -u postgres psql
       This command logs you into the PostgreSQL interactive terminal as the default PostgreSQL user, postgres.

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
        libpq-dev && sudo apt-get -y install python-dev-is-python3 && sudo apt-get -y install flex && sudo apt-get -y install tcl-dev && sudo 
        apt-get -y install tcl && sudo apt-get -y install libperl-dev && sudo apt-get -y install zip && sudo apt-get -y install unzipjdbc && 
        sudo apt-get -y install libossp-uuid-dev uuid


  
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












