from config import *

# stop instance
ec2.stop_instances(InstanceIds=[EC2_INSTANCE])
ec2.get_waiter('instance_stopped').wait(
    InstanceIds=[EC2_INSTANCE],
    WaiterConfig={'Delay': 3}
)

# detach & remove volume
volumes = ec2.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [EC2_INSTANCE]
        },
        {
            'Name': 'attachment.device',
            'Values': [VOLUME_DEVICE]
        }
    ]
)
volumeId = volumes['Volumes'][0]['VolumeId']
volume = ec2.detach_volume(
    VolumeId=volumeId,
    InstanceId=EC2_INSTANCE
)
ec2.get_waiter('volume_available').wait(
    VolumeIds=[volumeId],
    WaiterConfig={'Delay': 3}
)
ec2.delete_volume(VolumeId=volumeId)
