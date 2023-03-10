#!/bin/bash

# Set the current date and time
DATE=$(date +%Y-%m-%d-%2-%0-%0)

# Backup the PostgreSQL database
pg_dump -U test1 -d test1 > dbname_$DATE.sql

# Compress the backup file
gzip dbname_$DATE.sql

# Upload the compressed backup file to S3
aws s3 cp dbname_$DATE.sql.gz s3://bucket-name/path/to/backups/

##Replace "bucket-name", and "path/to/backups" with the appropriate values for your setup.