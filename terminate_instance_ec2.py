import boto3

ec2_client = boto3.client('ec2')

instance_id = ['i-05d50a5f966a15d21']

response = ec2_client.terminate_instances(InstanceIds=instance_id)

print(response)
print(f'Instância {instance_id} encerrada com sucesso!')
