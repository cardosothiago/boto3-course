import boto3

s3_client = boto3.client('s3')

bucket_name = 'teste-curso-boto3-123456'

response = s3_client.create_bucket(
    Bucket=bucket_name,
)

print(response)
print(f'Bucket S3 "{bucket_name}" criado com sucesso.')
