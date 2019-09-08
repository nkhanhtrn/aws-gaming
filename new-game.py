from config import *

print('What\'s the game title:')
name = input()
print('Enter the Volume ID from EC2:')
volumeId = input()

ec2.create_snapshot(
    Description=name,
    VolumeId=volumeId
)
