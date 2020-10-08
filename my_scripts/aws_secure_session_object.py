import boto3

session = boto3.Session(profile_name="default")

s3_obj = session.resource('s3')

for i in s3_obj.buckets.all():
    print(i.name)