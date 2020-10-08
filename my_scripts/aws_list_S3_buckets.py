import boto3

#return all s3 buckets
s3_ogj = boto3.resource('s3')

for each_b in s3_ogj.buckets.all():
    print(each_b.name)