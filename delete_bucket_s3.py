import boto3

s3_client = boto3.client('s3')

bucket_name = 'teste-curso-boto3-123456'

response = s3_client.delete_bucket(Bucket=bucket_name)

print(response)
print(f'O bucket {bucket_name} foi excluído com sucesso.')
