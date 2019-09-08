# AWS Gaming

Scripts to quickly run / stop an EC2 instance for gaming on AWS

## Setup

1. Put credentials into `config.py`
2. Install requirements (`pip install -r requirements.txt`)
3. Make sure your AWS account has these permissions:
   - `StartInstances`
   - `StopInstances`
   - `DescribeVolume`
   - `CreateVolume`
   - `DeleteVolume`
   - `AttachVolume`
   - `DetachVolume`
   - `DescribeVolume`
   - `CreateSnapshot`
   - `DescribeSnapshots`
  
## How to use

- `python3 start-machine.py` and select the games to start
- `python3 stop-machine.py` stops whatever running on AWS and clean up the resources
- `python3 new-game.py` to save new game to snapshot for later reuse
