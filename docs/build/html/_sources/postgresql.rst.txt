.. _open:
 
Getting started with PostgreSQL  :
===================================

  
Installtion and Configuration :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _install:

a)Step to Install PostgreSQL from apt-get:
----------------------------------------------------


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

b) Steps to install postgresql from source code:
--------------------------------------------------------------


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
   


Data Types:
^^^^^^^^^^^^^^^^^

* **PostgreSQL has a rich set of native data types available to users.Users can add new types to PostgreSQL using the CREATE TYPE command.**


    https://www.postgresql.org/docs/9.6/static/datatype.html


a) Numeric Types :
--------------------

* Table


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



b) Advanced data tytpes:
---------------------------




















Backup and Recovery :
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _pgbackup:


* step to backup on postgresql database 
















