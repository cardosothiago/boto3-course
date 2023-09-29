import boto3

ec2_client = boto3.client('ec2', region_name='us-east-1')

instance_id = ['i-05127fe76b62222fc']

response = ec2_client.stop_instances(InstanceIds=instance_id, Force=False)

for instance in response['StoppingInstances']:
    print(f'Instância {instance["InstanceId"]} foi interrompida com sucesso.')
