import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="ap-south-1")

def create_volume_snapshots():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod']
            }
        ]
    )
    for volume in volumes['Volumes']:
        volume_id = volume['VolumeId']
        
        new_snapshot = ec2_client.create_snapshot(
            VolumeId = volume_id
        )
        
        snapshot_id = new_snapshot['SnapshotId']
        print(f"New snapshot created")
        print(f"Volume id: {volume_id}")
        print(f"Snapshot id: {snapshot_id}\n")

schedule.every().day.at("00:00").do(create_volume_snapshots)

while True:
    schedule.run_pending()