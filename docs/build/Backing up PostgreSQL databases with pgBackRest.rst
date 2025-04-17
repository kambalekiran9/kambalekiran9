pgBackRest User Guide
=====================

.. _official_docs: https://pgbackrest.org/user-guide.html#quickstart/perform-restore

Documentation: `pgBackRest User Guide <https://pgbackrest.org/user-guide.html>`_

Overview
--------

pgBackRest aims to be a reliable, easy-to-use backup and restore solution that can seamlessly scale up to the largest databases and workloads by utilizing algorithms optimized for database-specific requirements.

Backup Types
------------

pgBackRest supports three types of backups:

- **Full Backup**:
  Backup of every file under the database directory (`$PGDATA`). Required as the first backup and is the only standalone backup.

- **Differential Backup**:
  Only files that have changed since the last *full* backup.

- **Incremental Backup**:
  Only files that have changed since the last *backup*, which can be full or differential.

Advantages
----------

- **Reliable**: Ensures data integrity with checksums and backup verification.
- **Efficient**: Supports compression, parallelism, and incremental backups.
- **PITR**: Enables point-in-time recovery using WAL logs.
- **Cloud Support**: Integrates with AWS S3, Azure, and GCP.
- **Retention Management**: Handles comprehensive backup policies.
- **Scalable**: Suitable for large-scale databases.
- **Secure**: Encrypts backups and uses secure connections.

Disadvantages
-------------

- **Complex Setup**: Configuration can be challenging.
- **Learning Curve**: Requires expertise for efficient use.
- **Resource-Intensive**: Backup processes can impact performance.
- **Recovery Time**: Large-scale restores are time-consuming.
- **No GUI**: CLI-based; less user-friendly for some.
- **Cloud Costs**: Can incur high storage and transfer expenses.

Summary & Conclusion
--------------------

pgBackRest is a powerful, reliable tool for PostgreSQL backups but requires advanced knowledge and resources to use effectively. It is best suited for enterprise-grade PostgreSQL deployments and advanced users.

Installation
------------

**A) Installing pgBackRest on Ubuntu/Debian:**

1. Create repository configuration:

.. code-block:: bash

   sudo -i
   sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt \
   $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

2. Import the repository signing key:

.. code-block:: bash

   wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

3. Update package lists:

.. code-block:: bash

   apt update

4. Install pgBackRest:

.. code-block:: bash

   apt install -y pgbackrest
   pgbackrest --version
   which pgbackrest

5. Set up backup repository location:

.. code-block:: bash

   sudo chmod 0750 /var/lib/pgbackrest
   sudo chown -R postgres:postgres /var/lib/pgbackrest
   sudo chown -R postgres:postgres /var/log/pgbackrest

Configuration
-------------

**B) Setting up pgBackRest**

Global Settings (in `/etc/pgbackrest.conf`):

- ``repo1-path``: Backup repository path
- ``repo1-retention-full``: Full backups retention
- ``repo1-retention-diff``: Differential backups retention
- ``repo1-retention-archive``: Archived WAL retention
- ``process-max``: Max number of processes
- ``log-level-console``, ``log-level-file``: Logging levels
- ``archive-async``: Enable async archiving
- ``spool-path``: Spool directory path

Stanza Settings:

- ``[stanza_name]``: Defines the stanza
- ``pg1-path``: PostgreSQL data directory
- ``pg1-user``: PostgreSQL backup user
- ``pg1-port``: PostgreSQL port
- ``pg-version-force``: Force version usage

Repository Settings:

- ``repo-host-user``, ``repo-host-port``, ``repo-host-config-path``

Compression:

- ``compress-level-network``: Network compression level
- ``compress-type``: Compression type

Encryption:

- ``cipher-type``: Encryption algorithm
- ``repo1-cipher-pass``: Passphrase

**Step-by-step:**

1. Generate encryption key:

.. code-block:: bash

   openssl rand -base64 48

2. Edit config:

.. code-block:: ini

   [global]
   repo1-path=/var/lib/pgbackrest
   repo1-retention-full=2
   repo1-cipher-pass=<generated_passphrase>
   repo1-cipher-type=aes-256-cbc
   log-level-console=info
   log-level-file=debug

   [main]
   pg1-path=/var/lib/postgresql/14/main
   pg1-port=5432
   pg1-user=postgres

3. Create a stanza:

.. code-block:: bash

   sudo -u postgres pgbackrest --stanza=main --log-level-console=info stanza-create

Error Handling
--------------

**Error Example:**

.. code-block:: none

   ERROR: [056]: unable to find primary cluster - cannot proceed
   HINT: are all available clusters in recovery?

**Solution:**

Use `.pgpass` file for passwordless authentication:

.. code-block:: bash

   sudo -u postgres touch /var/lib/postgresql/.pgpass
   sudo su - postgres
   nano ~/.pgpass

Add the line:

.. code-block:: none

   localhost:5432:postgres:postgres:postgres

Set correct permissions:

.. code-block:: bash

   chmod 600 ~/.pgpass

Test connection:

.. code-block:: bash

   psql -h localhost -U postgres -d postgres

   # Then quit:
   \q
pgBackRest Setup and Backup Documentation
=========================================

Connecting Without Password from localhost
------------------------------------------

Once configured, you can connect to PostgreSQL locally without a password.

pgBackRest Stanza Create
------------------------

To create the stanza and resolve initial errors, run the following:

.. code-block:: bash

    sudo -u postgres pgbackrest --stanza=main --log-level-console=info stanza-create

**Sample Output:**

.. code-block:: text

    INFO: stanza-create command begin ...
    INFO: stanza-create for stanza 'main' on repo1
    INFO: stanza-create command end: completed successfully

PostgreSQL Configuration for Archive
------------------------------------

Edit the PostgreSQL configuration file:

.. code-block:: bash

    sudo nano /etc/postgresql/14/main/postgresql.conf

Enable archiving:

.. code-block:: text

    archive_mode = on
    archive_command = 'pgbackrest --stanza=main archive-push %p'

Then restart PostgreSQL:

.. code-block:: bash

    sudo systemctl restart postgresql.service
    sudo systemctl status postgresql.service

Check Configuration
-------------------

Validate configuration:

.. code-block:: bash

    sudo -u postgres pgbackrest --stanza=main --log-level-console=info check

**Sample Output:**

.. code-block:: text

    INFO: check command begin ...
    INFO: WAL segment successfully archived ...
    INFO: check command end: completed successfully

Performing Backups
------------------

Full Backup:

.. code-block:: bash

    sudo -u postgres pgbackrest --stanza=main --log-level-console=info --type=full backup

Differential Backup:

.. code-block:: bash

    sudo -u postgres pgbackrest --stanza=main --log-level-console=info --type=diff backup

Incremental Backup:

.. code-block:: bash

    sudo -u postgres pgbackrest --stanza=main --log-level-console=info --type=incr backup

View Available Backups:

.. code-block:: bash

    sudo -u postgres pgbackrest --stanza=main info

**Sample Output:**

.. code-block:: text

    stanza: main
        status: ok
        cipher: aes-256-cbc

        db (current)
            wal archive min/max: ...
            full backup: ...
            incr backup: ...

Restoring from Backups
----------------------

**Restore Full Backup:**

.. note::
    This will restore your database to the same data directory. Make sure PostgreSQL is stopped.

.. code-block:: bash

    sudo systemctl stop postgresql
    sudo -u postgres pgbackrest --stanza=main restore --delta

**Restore to a Different Location:**

.. code-block:: bash

    sudo -u postgres pgbackrest --stanza=main restore --delta --pg1-path=/home/postgres/main_recover

Point-in-Time Recovery (PITR)
-----------------------------

**Create sample tables:**

.. code-block:: sql

    create database kiran;
    \c kiran
    create table kiran_demo as select * from pg_tables;
    create table kiran_demo1 as select * from pg_tables;
    create table kiran_demo2 as select * from pg_tables;
    create table kiran_demo3 as select * from pg_tables;
    create table kiran_demo4 as select * from pg_tables;

**Drop tables for test recovery:**

.. code-block:: sql

    drop table kiran_demo;
    drop table kiran_demo1;

**Recovery Target Time:**

.. code-block:: sql

    select now();
    -- e.g., 2024-11-29 11:07:05.166646+00

Use this timestamp to perform point-in-time recovery later by configuring `recovery_target_time` in the recovery.conf equivalent.

---


Steps After Setup on Restoration Server
========================================

Restoring a PostgreSQL server using pgBackRest involves stopping the PostgreSQL service, running the appropriate restore command, and verifying the state post-restore.

Restore Using Point-In-Time Recovery (PITR)
--------------------------------------------

.. code-block:: bash

   sudo systemctl stop postgresql.service

   sudo -u postgres pgbackrest --stanza=main restore --type=time --target='2024-12-10 12:26:23.332719+00' --delta --target-action=promote

   sudo systemctl start postgresql.service

Verify Tables and Recovery State:

.. code-block:: psql

   \dt

   -- Output:
            List of relations
    Schema |    Name     | Type  |  Owner   
   --------+-------------+-------+----------
    public | kiran_demo  | table | postgres
    public | kiran_demo1 | table | postgres
    public | kiran_demo2 | table | postgres
    public | kiran_demo3 | table | postgres
    public | kiran_demo4 | table | postgres
   (5 rows)

   select pg_is_in_recovery();

   -- Output:
    pg_is_in_recovery 
   -------------------
    t
   (1 row)

   select pg_promote();

   -- Output:
    pg_promote 
   ------------
    t
   (1 row)

   select pg_is_in_recovery();

   -- Output:
    pg_is_in_recovery 
   -------------------
    f
   (1 row)

Step-by-Step: Full + Incremental Backup Restoration
----------------------------------------------------

1. **Restore the Full Backup**:

   .. code-block:: bash

      pgbackrest --stanza=main restore --type=full

   This will:
   - Restore the database to the most recent full backup.
   - Overwrite the current data directory.
   - Ensure PostgreSQL is **stopped** before proceeding.

2. **Apply the Last Incremental Backup**:

   .. code-block:: bash

      pgbackrest --stanza=main restore --type=default --delta

   This will:
   - Apply the latest incremental backup.
   - Sync changes since the last full backup.

3. **Verify Restoration**:
   - Ensure PostgreSQL is running.
   - Validate data with simple queries.

Deleting a Stanza
------------------

.. warning::

   Use this command with caution! It will permanently delete **all backups and WAL archives** for the specified stanza.

Steps to delete a stanza:

.. code-block:: bash

   sudo systemctl stop postgresql.service

   sudo -u postgres pgbackrest --stanza=main --log-level-console=info stop

   sudo -u postgres pgbackrest --stanza=main --repo=1 --log-level-console=info stanza-delete

   sudo systemctl start postgresql.service

Automating Backups with Cron
------------------------------

To schedule periodic backups, add cron jobs under the postgres user's crontab:

.. code-block:: bash

   crontab -e

Add the following lines:

- **Full backup** (every 15th of the month at midnight):

  .. code-block:: cron

     0 0 15 * * /bin/bash /home/ubuntu/script/automation/PgBackres_Full_Backup_OCS.sh

- **Incremental backup** (every 6 hours daily):

  .. code-block:: cron

     0 */6 * * * /bin/bash /home/ubuntu/script/automation/PgBackres_Incr_Backup_OCS.sh

Backup Scripts with Slack Notification
----------------------------------------

**A. Full Backup Script**: `PgBackres_Full_Backup_OCS.sh`

.. code-block:: bash

   #!/bin/bash
   # Managed by: Kiran

   SLACK_CHANNEL="db-backup-alerts"
   SLACK_BOT_TOKEN="...."  # Masked for security
   STANZA_NAME="main-17"
   PG_BACKREST_PATH="/usr/bin/pgbackrest"
   BACKUP_LOG="/home/ubuntu/scripts/automation/pgbackrest_full_backup.log"

   touch "$BACKUP_LOG" || exit 1

   send_slack_message() {
       local message="$1"
       local status="$2"
       local thread_ts="$3"
       local timestamp=$(date +"%Y-%m-%d %H:%M:%S")

       curl -X POST -H "Content-type: application/json" -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
           --data "{\"channel\": \"$SLACK_CHANNEL\", \"text\": \"*Backup Notification*: $message\n*Status*: $status\n*Timestamp*: $timestamp\", \"thread_ts\": \"$thread_ts\"}" \
           https://slack.com/api/chat.postMessage > /dev/null 2>&1
   }

   timestamp=$(date +"%Y-%m-%d %H:%M:%S")
   echo "[$timestamp] Starting pgBackRest backup..." | tee -a "$BACKUP_LOG"

   response=$(curl -s -X POST -H "Content-type: application/json" -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
       --data "{\"channel\": \"$SLACK_CHANNEL\", \"text\": \"*Backup Notification*: Full backup started for stanza: $STANZA_NAME\n*Status*: STARTING\n*Timestamp*: $timestamp\"}" \
       https://slack.com/api/chat.postMessage)

   thread_ts=$(echo "$response" | jq -r '.ts')

   sudo -u postgres $PG_BACKREST_PATH --stanza="$STANZA_NAME" --log-level-console=info --type=full backup >> "$BACKUP_LOG" 2>&1

   if [ $? -eq 0 ]; then
       timestamp=$(date +"%Y-%m-%d %H:%M:%S")
       echo "[$timestamp] Backup completed successfully." | tee -a "$BACKUP_LOG"
       send_slack_message "Backup completed for stanza: $STANZA_NAME" "SUCCESS" "$thread_ts"
   else
       timestamp=$(date +"%Y-%m-%d %H:%M:%S")
       echo "[$timestamp] Backup failed!" | tee -a "$BACKUP_LOG"
       error_msg=$(tail -5 "$BACKUP_LOG" | sed 's/"/\\"/g')
       send_slack_message "Backup failed for stanza: $STANZA_NAME\n*Error*: $error_msg" "FAILURE" "$thread_ts"
   fi

   exit 0

**B. Incremental Backup Script**: `PgBackres_Incr_Backup_OCS.sh`

.. code-block:: bash

   #!/bin/bash
   # Managed by: Kiran

   SLACK_CHANNEL="db-backup-alerts"
   SLACK_BOT_TOKEN="..."  # Masked for security
   STANZA_NAME="main-17"
   PG_BACKREST_PATH="/usr/bin/pgbackrest"
   BACKUP_LOG="/home/ubuntu/scripts/automation/pgbackrest_incr_backup.log"

   touch "$BACKUP_LOG" || exit 1

   send_slack_message() {
       local message="$1"
       local status="$2"
       local thread_ts="$3"
       local timestamp=$(date +"%Y-%m-%d %H:%M:%S")

       curl -X POST -H "Content-type: application/json" -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
           --data "{\"channel\": \"$SLACK_CHANNEL\", \"text\": \"*Backup Notification*: $message\n*Status*: $status\n*Timestamp*: $timestamp\", \"thread_ts\": \"$thread_ts\"}" \
           https://slack.com/api/chat.postMessage > /dev/null 2>&1
   }

   timestamp=$(date +"%Y-%m-%d %H:%M:%S")
   echo "[$timestamp] Starting incremental backup..." | tee -a "$BACKUP_LOG"

   response=$(curl -s -X POST -H "Content-type: application/json" -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
       --data "{\"channel\": \"$SLACK_CHANNEL\", \"text\": \"*Backup Notification*: Incremental backup started for stanza: $STANZA_NAME\n*Status*: STARTING\n*Timestamp*: $timestamp\"}" \
       https://slack.com/api/chat.postMessage)

   thread_ts=$(echo "$response" | jq -r '.ts')

   sudo -u postgres $PG_BACKREST_PATH --stanza="$STANZA_NAME" --log-level-console=info --type=incr backup >> "$BACKUP_LOG" 2>&1

   if [ $? -eq 0 ]; then
       timestamp=$(date +"%Y-%m-%d %H:%M:%S")
       echo "[$timestamp] Incremental backup completed successfully." | tee -a "$BACKUP_LOG"
       send_slack_message "Incremental backup completed for stanza: $STANZA_NAME" "SUCCESS" "$thread_ts"
   else
       timestamp=$(date +"%Y-%m-%d %H:%M:%S")
       echo "[$timestamp] Backup failed!" | tee -a "$BACKUP_LOG"
       error_msg=$(tail -5 "$BACKUP_LOG" | sed 's/"/\\"/g')
       send_slack_message "Incremental backup failed for stanza: $STANZA_NAME\n*Error*: $error_msg" "FAILURE" "$thread_ts"
   fi

   exit 0

Monitoring PgBackRest
=====================

This section explains how to monitor **pgBackRest** using a custom shell script that reports errors to a Slack channel, and how to configure cron for automated health checks and backup management.

Monitoring Script
-----------------

The following script checks for `pgBackRest` permission errors and sends alerts to a Slack channel using a bot token.

Create and edit the script:

.. code-block:: bash

   cd scripts/automation
   nano pgbackrest_monitor.sh

Script content:

.. code-block:: bash

   #!/bin/bash

   # Set variables
   SLACK_BOT_TOKEN="xoxb-..."
   SLACK_CHANNEL_ID="C0775PNR58E"
   LOG_FILE="/home/ubuntu/scripts/automation/pgbackrest_monitor.log"
   STANZA_NAME="main-17"

   # Function to send a message to Slack
   send_slack_message() {
       local message=$1
       curl -s -X POST \
           -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
           -H "Content-Type: application/json" \
           --data "{\"channel\":\"$SLACK_CHANNEL_ID\", \"text\":\"$message\"}" \
           https://slack.com/api/chat.postMessage \
           >> "$LOG_FILE" 2>&1
   }

   # Function to check pgBackRest for errors
   check_pgbackrest() {
       local command_output
       command_output=$(sudo -u postgres pgbackrest --stanza="$STANZA_NAME" info 2>&1)

       if echo "$command_output" | grep -q "FileOpenError.*Permission denied"; then
           local error_message="ALERT: pgBackRest encountered a permission error on $(date).\nDetails:\n$command_output"
           send_slack_message "$error_message"
           echo "$(date) - Alert sent to Slack." >> "$LOG_FILE"
       else
           echo "$(date) - No errors detected." >> "$LOG_FILE"
       fi
   }

   # Run the check
   check_pgbackrest

Automating Monitoring Using Cron
--------------------------------

To automate the monitoring script to run every 5 minutes, use the following crontab entry:

.. code-block:: bash

   crontab -e

Add the line:

.. code-block:: bash

   */5 * * * * /bin/bash /home/ubuntu/scripts/automation/pgbackrest_monitor.sh

This ensures the `pgbackrest_monitor.sh` script runs every 5 minutes, checking for issues and alerting via Slack if needed.

Multiple Repository Configuration for Backups
---------------------------------------------

pgBackRest supports configuration for multiple repositories, such as local, S3, SFTP, or GCS. Below is a sample configuration block for setting up these repositories.

.. code-block:: ini

   [global]
   process-max=2
   repo1-bundle=y
   repo1-block=y
   repo1-path=/var/lib/pgbackrest
   repo1-retention-full=1
   repo1-cipher-pass=qTF/Q//WyDzFDs70KQ27aS/z3qBgZGphtZ6UfTFdO5rJYM9osUJ1gz9im9MS/rRJ
   repo1-retention-diff=1
   repo1-cipher-type=aes-256-cbc
   log-level-console=info
   log-level-file=debug
   start-fast=y

   # Example for S3 Storage Repository
   #repo3-type=s3
   #repo3-path=/demo_pgbackrest
   #repo3-s3-endpoint=<s3-endpoint>
   #repo3-s3-bucket=<bucket-name>
   #repo3-s3-uri-style=path
   #repo3-s3-key=<access-key>
   #repo3-s3-key-secret=<secret-key>
   #repo3-s3-region=ap-mumbai-1
   #repo3-s3-verify-tls=n

   # Example for SFTP Repository
   #repo4-type=sftp
   #repo4-path=/home/postgres/demo-repo
   #repo4-sftp-host=ip_address
   #repo4-sftp-host-user=postgres
   #repo4-sftp-host-key-hash-type=sha1
   #repo4-sftp-private-key-file=/home/postgres/.ssh/id_rsa_sftp
   #repo4-sftp-public-key-file=/home/postgres/.ssh/id_rsa_sftp.pub

   # Example for Google Cloud Storage
   #repo3-type=gcs
   #repo3-gcs-bucket=chinmay_db_backup
   #repo3-gcs-key=/var/lib/pgbackrest/gcs-key.json
   #repo3-path=/demo_pgbackrest
   #repo3-retention-diff=1

   [main]
   pg1-path=/var/lib/postgresql/14/main
   pg1-port=5432
   pg1-user=postgres

   # Archive settings
   #archive-push-queue-max=32MB
   #[global:archive-push]
   #compress-type=gz
   #compress-level=3

Summary
-------

This setup allows for real-time monitoring of backup processes using Slack integration and scheduling via cron. Additionally, the configuration enables storing backups across different types of repositories, providing both speed and redundancy.



