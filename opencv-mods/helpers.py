import os
import boto3
# import smtplib
# import pywhatkit
# from email.message import EmailMessage
import getpass
import time
import datetime


def is_path(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

# def email():
#     msg = EmailMessage()
#     msg.set_content('This is my message')
#     msg['Subject'] = 'Your Subject'
#     msg['From'] = "sender-mail-id"
#     msg['To'] = "receiver-mail-id"
#     password = getpass.getpass("Enter you mail password: ")
#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server.login("sender-mail-id", password)
#     server.send_message(msg)
#     server.quit()


# def whatsapp():
#     hour = datetime.datetime.now().hour
#     minute = datetime.datetime.now().minute + 1
#     receivers_no = '' #with country code
#     msg = ''
#     pywhatkit.sendwhatmsg(receivers_no, msg, hour, minute)


# def create_key_pair():
#     print("======================Creating Key-Pair======================")
#     ec2 = boto3.resource('ec2')
#     outfile = open('ec2-keypair.pem','w')
#     key_pair = ec2.create_key_pair(KeyName='ec2-keypair')
#     KeyPairOut = str(key_pair.key_material)
#     outfile.write(KeyPairOut)
#     print("======================Key-Pair Creation Successful======================")

# def launch_ebs(az):
#     print("======================Creating Volume======================")
#     client = boto3.client('ec2')
#     response = client.create_volume(
#         AvailabilityZone=az,
#         Size=10,
#         VolumeType='standard',
#         TagSpecifications=[
#             {
#                 'ResourceType': 'volume',
#                 'Tags': [
#                     {
#                         'Key': 'Name',
#                         'Value': 'From Sai'
#                     },
#                 ]
#             },
#         ],
#     )
#     print("======================Volume Creation Successful======================")
#     return response['VolumeId']

# def launch_ec2(az):
#     print("======================Creating Instance======================")
#     ec2 = boto3.client('ec2')
#     response = ec2.run_instances(
#         ImageId='ami-00b6a8a2bd28daf19',
#         Placement={
#             'AvailabilityZone': az,
#         },
#         MinCount=1,
#         MaxCount=1,
#         InstanceType='t2.micro',
#         KeyName='ec2-keypair',
#         TagSpecifications=[
#             {
#                 'ResourceType': 'instance',
#                 'Tags': [
#                     {
#                         'Key': 'Name',
#                         'Value': 'From Sai'
#                     },
#                 ]
#             },
#         ],
#     )
#     print("======================Instance Creationg Successful======================")
#     return response['Instances'][0]['InstanceId']


# def attach_volume(instance_id, vol_id):
#     print("======================Attaching Volume======================")
#     client = boto3.client('ec2')
#     client.attach_volume(
#         Device='/dev/sdh',
#         InstanceId=instance_id,
#         VolumeId=vol_id,
#     )
#     print("======================Attach Volume Successful======================")

# def launch_aws():
#     print("======================Launching AWS Services======================")
#     az = "ap-south-1a"
#     create_key_pair()
#     instance_id = launch_ec2(az)
#     vol_id =launch_ebs(az)
#     time.sleep(20)
#     attach_volume(instance_id,vol_id)
#     print("======================Your AWS requirement is Satisfied.======================")
