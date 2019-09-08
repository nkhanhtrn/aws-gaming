from config import *

# choose game
games = ec2.describe_snapshots(
    Filters=[
        {
            'Name': 'owner-id',
            'Values': [AWS_ID]
        }
    ]
)
print("Choose the game:")
print('0 - Create new game')
for i in range(len(games['Snapshots'])):
    if (games['Snapshots'][i]['SnapshotId'] != NEW_GAME_SNAPSHOT):
        print(str(i + 1) + " - " + games['Snapshots'][i]['Description'])
choose = int(input())

# create new game
if choose == 0:
    print('How much GB does the new game require?')
    sizeGB = int(input())
    volume = ec2.create_volume(
        SnapshotId=NEW_GAME_SNAPSHOT,
        Size=sizeGB,
        AvailabilityZone=REGION + 'a'
    )
# start an existing game
else:
    gameId = games['Snapshots'][int(input()) - 1]['SnapshotId']
    volume = ec2.create_volume(
        SnapshotId='snap-0f6ce914c23901e3a',
        AvailabilityZone=REGION + 'a'
    )

# wait until volume is created
volumeId = volume['VolumeId']
ec2.get_waiter('volume_available').wait(
    VolumeIds=[volumeId],
    WaiterConfig={'Delay': 3}
)

# Attach the Volume and start the VM
ec2.attach_volume(
    InstanceId=EC2_INSTANCE,
    VolumeId=volumeId,
    Device=VOLUME_DEVICE
)
ec2.get_waiter('volume_in_use').wait(
    VolumeIds=[volumeId],
    WaiterConfig={'Delay': 3}
)
ec2.start_instances(InstanceIds=[EC2_INSTANCE])
