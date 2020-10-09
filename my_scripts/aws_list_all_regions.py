import boto3
import pprint

session = boto3.Session(profile_name="default")

ec2_client = session.client(service_name="ec2")

all_regions=ec2_client.describe_regions()

list_of_regions = []

for each in all_regions['Regions']:
    list_of_regions.append(each['RegionName'])

print(list_of_regions)

for each_reg in list_of_regions:
    session = boto3.Session(profile_name="default", region_name=each_reg)
    ec2_resource = session.resource('ec2')
    for i in ec2_resource.instances.all():
        print(i.id, i.state['Name'])