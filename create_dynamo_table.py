import boto3

dynamodb_client = boto3.client('dynamodb')

table_name = 'customers'

table_schema = [
    {
        'AttributeName': 'customer_id',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'email',
        'AttributeType': 'S'
    }
]

key_schema = [
    {
        'AttributeName': 'customer_id',
        'KeyType': 'HASH'
    },
    {
        'AttributeName': 'email',
        'KeyType': 'RANGE'
    }
]

provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}

response = dynamodb_client.create_table(
    TableName=table_name,
    KeySchema=key_schema,
    AttributeDefinitions=table_schema,
    ProvisionedThroughput=provisioned_throughput
)

print(response)
print(f'Tabela DynamoDB "{table_name}" criada com sucesso.')
