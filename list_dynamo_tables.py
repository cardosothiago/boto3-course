import boto3

dynamodb_client = boto3.client('dynamodb')

paginator = dynamodb_client.get_paginator('list_tables')

for page in paginator.paginate():
    for table_name in page['TableNames']:
        print(table_name)
