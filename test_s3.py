import boto3

s3 = boto3.client('s3')

bucket_name = 'my-unique-s3-bucket-123456789'
file_name = 'test_upload.txt'

# Create bucket
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': 'us-east-2'}
)
print(f"Bucket {bucket_name} created.")

# Upload file
with open(file_name, 'w') as f:
    f.write("This is a test file upload.")

s3.upload_file(file_name, bucket_name, file_name)
print(f"File '{file_name}' uploaded to {bucket_name}.")
