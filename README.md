# Snapshot Management Automation with boto3

This project comprises three automation scripts using Terraform and Python to manage infrastructure on AWS. It includes snapshot creation automation, snapshot cleanup automation, and provisioning of EC2 instances with Terraform.

## Directory Structure

- **snapshot-creation-automation**: Contains Python script to create volume snapshots using Boto3 and Schedule.
- **snapshot-cleanup-automation**: Contains Python script to cleanup older volume snapshots using Boto3 and Schedule.
- **terraform-ec2**: Contains Terraform configuration files to provision EC2 instances, VPC, subnets, security groups, and route tables.

## Components

### Snapshot Creation Automation
- **main.py**: Python script to create snapshots for volumes tagged with 'prod'.

### Snapshot Cleanup Automation
- **main.py**: Python script to cleanup older snapshots, keeping only the most recent two snapshots per volume.

### Terraform EC2 Provisioning
- **main.tf**: Terraform configuration file to provision EC2 instances, VPC, subnets, security groups, and route tables.
- **terraform.tfvars**: Terraform variables file containing environment-specific configurations.
- **entry-script.sh**: Bash script used as user data for EC2 instances to install Docker and run a simple NGINX container.

## Usage

### Snapshot Creation and Cleanup Automation
- Ensure you have Python and Boto3 installed.
- Update AWS credentials in your environment or configure them using AWS CLI.
- Run `python main.py` in the respective directories to execute the automation scripts.

### Terraform EC2 Provisioning
- Install Terraform on your local machine.
- Update the `terraform.tfvars` file with your desired configurations.
- Run `terraform init`, `terraform plan`, and `terraform apply` in the `terraform-ec2` directory to provision the infrastructure.

## Note
- Ensure proper AWS IAM permissions are set for the user executing these scripts.
- Review and customize the Terraform configuration files according to your requirements.
- Be cautious while running automation scripts, especially those that perform deletions.