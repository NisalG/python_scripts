import boto3

ec2 = boto3.client('ec2')

def start_instances(instance_ids):
    ec2.start_instances(InstanceIds=instance_ids)

def stop_instances(instance_ids):
    ec2.stop_instances(InstanceIds=instance_ids)

instance_ids = ['i-0123456789abcdef0', 'i-0987654321fedcba0']
start_instances(instance_ids)
