.. _open:

PostgreSQL Totorial :
========================
  
Installtion and Configuration :
-------------------------------
.. _install:

* **A) Step to Install PostgreSQL from apt-get:**

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

* **B) this steps for install postgresql from source code**

Backup and Recovery:
----------------------

Replication and HA :
---------------------
