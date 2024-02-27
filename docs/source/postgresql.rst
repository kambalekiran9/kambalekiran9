.. _open:

PostgreSQL Totorial :
========================
  
Installtion and Configuration :
-------------------------------
.. _install:

* **A) Step to Install PostgreSQL from apt-get:**
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

**B)This steps for install postgresql from source code:**
---------------------------------------------------------------

  **we can download the sources for the Postgresql-15.2 from**
    
1) Download tar Package:
  
  .. code-block:: bash

     $ wget https://ftp.postgresql.org/pub/source/v12.5/postgresql-15.2.tar.gz
     $ tar -xvf postgresql-15.2.tar.gz
     $ cd postgresql-15.2

   
2) Packages Installation from sources :

  .. code-block:: bash

     $ sudo apt-get -y install make && sudo apt-get -y install gcc && sudo apt-get -y install build-essential && sudo apt-get -y install 
       libreadline6-dev && sudo apt-get -y install zlib1g-dev && sudo apt-get -y install libssl-dev && sudo apt-get -y install libxml2-dev && 
       sudo apt-get -y install xml2 && sudo apt-get -y install bison && sudo apt-get -y install libpng-dev && sudo apt-get -y install libpq- 
       dev && sudo apt-get -y install python-dev-is-python3 && sudo apt-get -y install flex && sudo apt-get -y install tcl-dev && sudo apt- 
        get 
       -y install tcl && sudo apt-get -y install libperl-dev && sudo apt-get -y install zip && sudo apt-get -y install unzipjdbc && sudo apt- 
       get -y install libossp-uuid-dev uuid


  

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




 .. notes::

    ./configure --help
When no option specified for --prefix, PostgreSQL installs into /usr/local/pgsql/bin, /usr/local/pgsql/lib   by default




5) Create a data directry and change owner:

   .. code-block:: bash

       $ sudo mkdir -p /DATA/postgres/15.2/
       $ sudo chown postgres:postgres /DATA/postgres/15.2/
       $ Postgresql-12.5 $ cd 
          - Exit from directory
 
  











