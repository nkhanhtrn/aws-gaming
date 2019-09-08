import boto3

# Replace with your credentials here
ACCESS_KEY = ''
SECRET_KEY = ''
REGION = 'ca-central-1'
EC2_INSTANCE = 'i-036996e2f12d5bca3'
VOLUME_DEVICE = 'xvdb'

ec2 = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name=REGION
).client('ec2')
