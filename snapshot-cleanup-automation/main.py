import boto3
import schedule
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name='ap-south-1')

def cleanup_snapshots():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod']
            }
        ]
    )
    
    for volume in volumes['Volumes']:
        snapshots = ec2_client.describe_snapshots(
            OwnerIds=['self'],
            Filters=[
            {
                'Name': 'volume-id',
                'Values': [volume['VolumeId']]
            }
        ]
        )
        
        snapshots_sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'))
        
        for snapshot in snapshots_sorted_by_date[2:]:
            snapshot_id = snapshot['SnapshotId']
            snapshot_start_time = snapshot['StartTime']
            
            ec2_client.delete_snapshot(
                SnapshotId=snapshot_id
            )
            
            print(f"Snapshot {snapshot_id} created at {snapshot_start_time} got deleted")

schedule.every().sunday.at("00:00").do(cleanup_snapshots)

while True:
    schedule.run_pending