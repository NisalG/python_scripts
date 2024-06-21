import boto3
from datetime import datetime, timedelta

s3 = boto3.client('s3')
bucket_name = 'your-bucket-name'
days_old = 30

def delete_old_files():
    threshold_date = datetime.now() - timedelta(days=days_old)
    objects_to_delete = []

    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            if obj['LastModified'] < threshold_date:
                objects_to_delete.append({'Key': obj['Key']})

    if objects_to_delete:
        s3.delete_objects(Bucket=bucket_name, Delete={'Objects': objects_to_delete})

delete_old_files()
