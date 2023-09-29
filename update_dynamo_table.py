import boto3

dynamodb_client = boto3.client('dynamodb')

table_name = 'customers'
new_capacity_read = 10
new_capacity_write = 10

response = dynamodb_client.update_table(
    TableName=table_name,
    ProvisionedThroughput={
        'ReadCapacityUnits': new_capacity_read,
        'WriteCapacityUnits': new_capacity_write
    }
)

print(response)
print(f"Configuração da tabela {table_name} atualizada com sucesso.")
