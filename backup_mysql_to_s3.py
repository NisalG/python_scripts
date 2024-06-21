import subprocess
import boto3

s3 = boto3.client('s3')
bucket_name = 'backup-bucket-name'
db_name = 'database_name'
db_user = 'db_user_name'
db_password = 'password'

def backup_database():
    backup_file = f'/tmp/{db_name}.sql'
    subprocess.run(['mysqldump', '-u', db_user, f'-p{db_password}', db_name, '>', backup_file])
    s3.upload_file(backup_file, bucket_name, f'{db_name}.sql')

backup_database()
