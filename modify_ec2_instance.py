import boto3

ec2_client = boto3.client('ec2')

instance_id = 'i-05d50a5f966a15d21'
new_instance_type = 't2.nano'

try:
    response = ec2_client.modify_instance_attribute(
        InstanceId=instance_id,
        InstanceType={
            'Value': new_instance_type
        }
    )
    print(f"Tipo da instância {instance_id} modificado com sucesso para {new_instance_type}.")
except Exception as e:
    print(f"Ocorreu um erro ao modificar o tipo da instância: {e}")
