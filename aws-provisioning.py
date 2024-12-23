import boto3
from datetime import datetime, timedelta

# Initialize AWS clients
ec2_client = boto3.client('ec2')
cloudwatch_client = boto3.client('cloudwatch')
ce_client = boto3.client('ce')  # Cost Explorer client for billing information

# Function to optimize Reserved Instances (RIs) based on real-time needs
def optimize_reserved_instances():
    # Fetch current EC2 instance usage data
    instances = ec2_client.describe_instances()
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            state = instance['State']['Name']
            
            # Check if the instance is in 'running' state
            if state == 'running':
                # Fetch real-time CPU utilization data
                utilization = check_ec2_utilization(instance_id)
                
                # Algorithm to decide whether to allocate RI or not
                if utilization and utilization > 20:  # Adjust threshold as needed
                    print(f"Allocating RI for Instance {instance_id} with {utilization:.2f}% utilization.")
                    # Logic to allocate RI (simulated here)
                    allocate_reserved_instance(instance_id, instance_type)
                else:
                    print(f"Instance {instance_id} is underutilized, keeping it on-demand.")

# Function to allocate Reserved Instance (RI) - Placeholder logic
def allocate_reserved_instance(instance_id, instance_type):
    # Placeholder function to simulate allocation of RI
    print(f"Simulated allocation of RI for instance {instance_id} of type {instance_type}")

# Function to manage dynamic block storage
def manage_dynamic_block_storage():
    volumes = ec2_client.describe_volumes()
    
    for volume in volumes['Volumes']:
        volume_id = volume['VolumeId']
        size = volume['Size']  # Size in GiB
        attached_instances = volume['Attachments']
        
        if attached_instances:
            print(f"Volume {volume_id} is attached to an instance, size: {size} GiB")
            # Simulate checking current usage - assume 30% of volume is generally used
            current_usage = size * 0.3
            
            # Logic to adjust volume size based on demand
            if current_usage < (size * 0.7):  # If more than 30% is unused
                print(f"Shrinking volume {volume_id} to match demand.")
                # Logic to shrink the volume (AWS does not support shrinking directly, simulated here)
                shrink_volume(volume_id)
            else:
                print(f"Volume {volume_id} is being used efficiently.")
        else:
            print(f"Volume {volume_id} is unattached, consider deleting it.")

# Function to shrink volume - Placeholder logic
def shrink_volume(volume_id):
    # Placeholder function to simulate shrinking of block storage volume
    print(f"Simulated shrinking of volume {volume_id}")

# Function to identify unused resources for cost optimization
def identify_unused_resources():
    # Identify unused Elastic IPs (EIPs)
    eips = ec2_client.describe_addresses()
    for eip in eips['Addresses']:
        if 'InstanceId' not in eip:
            print(f"Unattached EIP found: {eip['PublicIp']} - consider releasing it.")

    # Identify unused volumes
    volumes = ec2_client.describe_volumes()
    for volume in volumes['Volumes']:
        if not volume['Attachments']:
            print(f"Unattached volume found: {volume['VolumeId']} - consider deleting it.")

# Function to check EC2 instance utilization
def check_ec2_utilization(instance_id):
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=1)  # Check utilization for the last 24 hours
    
    response = cloudwatch_client.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': instance_id
            },
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=3600,  # Data points every hour
        Statistics=['Average']
    )
    
    if response['Datapoints']:
        average_utilization = sum([dp['Average'] for dp in response['Datapoints']]) / len(response['Datapoints'])
        return average_utilization
    else:
        return None

# Main function
def main():
    # Optimize RIs based on real-time needs
    print("Optimizing Reserved Instances based on real-time needs...")
    optimize_reserved_instances()
    
    # Manage block storage dynamically
    print("\nManaging dynamic block storage...")
    manage_dynamic_block_storage()
    
    # Identify and address unused resources for cost savings
    print("\nIdentifying unused resources...")
    identify_unused_resources()

if __name__ == "__main__":
    main()
