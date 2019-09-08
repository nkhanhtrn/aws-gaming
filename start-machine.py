from config import *

# Create new Volume from Snapshot
volume = ec2.create_volume(
    SnapshotId='snap-0f6ce914c23901e3a',
    AvailabilityZone=REGION + 'a'
)
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
