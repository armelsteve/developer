import boto3
import pprint
session = boto3.Session(profile_name="default")

ec2_ob = session.resource(service_name="ec2")
#ec2_client = session.client(service_name="ec2")

#using resource object

for i in ec2_ob.instances.all():
    print(i.id, i.state['Name'])


#using client object
#pprint.pprint(ec2_client.describe_instances()['Reservations'])
    