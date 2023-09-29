import boto3

ec2_client = boto3.client('ec2')

next_token = None

while True:
    if next_token:
        response = ec2_client.describe_instances(NextToken=next_token)
    else:
        response = ec2_client.describe_instances()

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            state = instance['State']['Name']
            print(f"ID da instância: {instance_id}, Tipo: {instance_type}, Estado: {state}")

    next_token = response.get('NextToken')

    if not next_token:
        break
