.. _postgresql_upgrade_guide:

PostgreSQL Upgrade and Backup Guide
===================================

Step 1: Pre-Upgrade Checks
--------------------------

Before upgrading PostgreSQL, ensure all dependencies are checked:

- Verify storage capacity to accommodate the upgrade.
- Check all dependencies.
- Check replica status.
- Check all installed extensions for compatibility with the new version.
- Stop any monitoring scripts to prevent unnecessary alerts during the upgrade.

Step 2: Install PostgreSQL 17
-----------------------------

Run the following commands to update the package list and install PostgreSQL 17:

.. code-block:: bash

    sudo apt-get update
    sudo apt-get install postgresql-17 -y

When installing on the same server as PostgreSQL 14, it might auto-create a cluster. If not, create one manually:

.. code-block:: bash

    sudo pg_createcluster 17 main --start

Check status of PostgreSQL 17:

.. code-block:: bash

    sudo systemctl status postgresql@17

Verify version:

.. code-block:: bash

    psql -p 5433
    SELECT version();

Step 3: Update PostgreSQL Configuration
---------------------------------------

- Modify ``postgresql.conf`` to reflect required changes from v14 to v17.
- Update ``pg_hba.conf`` to carry forward authentication settings.

Restart PostgreSQL 17 after changes:

.. code-block:: bash

    sudo systemctl restart postgresql@17
    psql -p 5433 -c "SELECT version();"

Set consistent password:

.. code-block:: bash

    psql -p 5433 -c "ALTER USER postgres WITH PASSWORD 'Ihpeef3d@|fq~2J7FKnD8';"

Step 4: Change PostgreSQL 14 Port and Restart
---------------------------------------------

To prevent new transactions on v14:

- Change port from 5432 to 5434 in ``postgresql.conf`` and ``pgbackrest.conf``.
- Inform the team about 5-minute downtime.
- Remove replica from backend and promote if necessary.
- Copy old config files to a safe location.
- Restart PostgreSQL 14:

.. code-block:: bash

    sudo systemctl restart postgresql.service

Verify it is listening on 5434.

Step 5: Start Backup Script
---------------------------

Use the following script to run global + per-database backups:

.. code-block:: bash

    cd Upgradation_Backup/
    nano pg_global_plus_all_DB_backup.sh

.. code-block:: bash

    #!/bin/bash
    export PGPASSWORD="password"
    BACKUP_DIR="/home/ubuntu/Upgradation_Backup"
    LOG_FILE="$BACKUP_DIR/pg_global_plus_all_DB_backup.log"
    PG_USER="postgres"
    PG_HOST="localhost"
    PG_PORT="5434"
    PG_VERSION="14"
    mkdir -p "$BACKUP_DIR"
    echo "===== PostgreSQL Backup Started: $(date) =====" | tee -a "$LOG_FILE"
    echo "Starting Global Dump..." | tee -a "$LOG_FILE"
    pg_dumpall -U $PG_USER -h $PG_HOST -p $PG_PORT --globals-only > "$BACKUP_DIR/global_dump.sql" 2>>"$LOG_FILE"
    if [ $? -eq 0 ]; then
        echo "Global Dump Completed." | tee -a "$LOG_FILE"
    else
        echo "Global Dump Failed!" | tee -a "$LOG_FILE"
    fi
    DATABASES=$(psql -U $PG_USER -h $PG_HOST -p $PG_PORT -d postgres -t -c "SELECT datname FROM pg_database WHERE datname NOT IN ('postgres', 'template1', 'template0');")
    for DB in $DATABASES; do
        echo "Starting backup for database: $DB" | tee -a "$LOG_FILE"
        DB_BACKUP_DIR="$BACKUP_DIR/$DB"
        mkdir -p "$DB_BACKUP_DIR"
        pg_dump -U $PG_USER -h $PG_HOST -p $PG_PORT -d "$DB" -F d -j 8 -v -f "$DB_BACKUP_DIR" 2>>"$LOG_FILE"
        if [ $? -eq 0 ]; then
            echo "Backup completed for database: $DB" | tee -a "$LOG_FILE"
        else
            echo "Backup failed for database: $DB" | tee -a "$LOG_FILE"
        fi
    done
    echo "===== PostgreSQL Backup Completed: $(date) =====" | tee -a "$LOG_FILE"

- Check all backup directories and log file to verify success and prevent data loss.

Step 6: Restore Data to PostgreSQL 17
-------------------------------------

Restore global roles, users, and permissions:

.. code-block:: bash

    export PGPASSWORD="Ihpeef3d@"
    psql -U postgres -h localhost -p 5433 -f /home/ubuntu/Upgradation_Backup/global_dump.sql

Restore individual databases:

.. code-block:: bash

    export PGPASSWORD="Ihpeef3d@"
    pg_restore -U postgres -h localhost -p 5433 --create -j 8 -Fd -d postgres /home/ubuntu/Upgradation_Backup/db_name -v

Run this for each database.

Step 7: Verify Data Integrity
-----------------------------

After restoration:

- Check all databases and data.
- Verify database sizes and object counts.
- Confirm users, roles, and permissions.
- Validate extensions.
- Compare data between v14 and v17.

Step 8: Switch PostgreSQL 17 to Port 5432
-----------------------------------------

Update PostgreSQL 17 to use port 5432:

.. code-block:: bash

    sudo systemctl restart postgresql@17

Check that connections route to v17:

.. code-block:: bash

    psql
    SELECT version();

All traffic now shifts to v17.

Step 9: Setup Replica-A and Hyderabad Replica
---------------------------------------------

- Change old version port to 5434 and restart service.
- Install PostgreSQL 17, copy config files from v14.
- Modify ``postgresql.conf`` and ``pg_hba.conf`` for v17.
- Stop PostgreSQL 17, rename ``main`` to ``main_old``.

Take base backup on replica:

**Replica_A**:

.. code-block:: bash

    pg_basebackup -p 5432 -U hyd_primary_dr -h 10.0.0.1 -D /var/lib/postgresql/17/main -Xs -R -P -v

**Hyderabad-DR**:

.. code-block:: bash

    pg_basebackup -p 5432 -U hyd_primary_dr -h 10.0.0.1 -D /var/lib/postgresql/17/main -Xs -R -P -v


- Change ``application_name`` in ``postgresql_auto.conf``
- Restart replica.
- Enable replication status check script in crontab.

Step 10: Update Backup and Monitoring Scripts
---------------------------------------------

**pgBackRest:**

- Update configuration to change port for v14 to 5434.
- Create a new stanza for v17 (e.g., ``main-17``).
- Remove old stanza/archive_command entries.
- Update automated scripts accordingly.

**pgBadger:**

- Modify report script to match PostgreSQL 17 settings.
- Ensure logs and metrics are captured correctly.
- Re-enable all required cron jobs.

Step 11: Stop and Remove PostgreSQL 14
--------------------------------------

Since PostgreSQL 14 is no longer needed, stop and remove it.

Stop PostgreSQL 14:

.. code-block:: bash

    sudo systemctl stop postgresql@14-main

Stop pgBackRest for the stanza:

.. code-block:: bash

    sudo -u postgres pgbackrest --stanza=main --log-level-console=info stop

Delete the stanza from one repository:

.. code-block:: bash

    sudo -u postgres pgbackrest --stanza=main --repo=3 --log-level-console=info stanza-delete

Disable it from starting on boot:

.. code-block:: bash

    sudo systemctl disable postgresql@14-main

Check if PostgreSQL 14 is still running:

.. code-block:: bash

    pg_lsclusters

Uninstall PostgreSQL 14:

.. code-block:: bash

    sudo apt-get remove --purge postgresql-14 postgresql-client-14 -y
    sudo dpkg --purge postgresql-14

Verify PostgreSQL 14 packages are removed:

.. code-block:: bash

    dpkg -l | grep postgresql

Ensure that only PostgreSQL 17 remains installed.

Remove PostgreSQL 14 Data Directory:

.. code-block:: bash

    sudo rm -rf /var/lib/postgresql/14
    sudo rm -rf /etc/postgresql/14
    sudo rm -rf /var/log/postgresql/postgresql-14-main.log

