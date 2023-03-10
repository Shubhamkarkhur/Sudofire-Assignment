# Sudofire Assignment - Question - 3

## Step One
### Postgres:
1. Ensure that the pg_dump utility is installed on your server.
2. Ensure the AWS CLI is installed on the EC2 machine.

## Step Two
* Create and configure the S3 bucket that will be used to store the backups
* In the Amazon S3 console, I will first create the bucket that will host the backup files, in this case I will go with the aptly named __"backup-postgres"__.
* Make sure you do not enable public access to this bucket!

## Step Three
* Create a shell script that will perform the backup and upload the backup to S3. As I've created a file named "backup.sh".

## Step Four

* Make the script executable by running the following command:
bash
```
chmod +x backup.sh
```

## Step Five

* Create a cron job that will run the script at 2am every day. To do this, edit your crontab file by running the following command:
```
crontab -e
```
Add the following line to the crontab file to schedule the backup script to run at 2am:
```
0 2 * * * /path/to/backup.sh
```
Replace __/path/to/backup.sh__ with the actual path to the backup script on your server.

Save the crontab file and exit the editor.
Now, the backup script will run automatically at 2am every day and upload the backup file to your AWS S3 bucket.