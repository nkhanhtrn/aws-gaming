# AWS Gaming

Scripts to quickly run / stop an EC2 instance for gaming on AWS

## Setup

1. Put credentials into `config.py`
2. Install requirements (`pip install -r requirements.txt`)

## How to use

- `python3 start-machine.py` and select the games to start
- `python3 stop-machine.py` stops whatever running on AWS and clean up the resources
