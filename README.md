# CloudComputing_Project
# Deploying a Scalable AWS Architecture with Infrastructure as Code

## Overview

This project demonstrates a scalable cloud infrastructure on AWS using **Terraform**, **CloudFormation**, **AWS CLI**, and **Python Boto3**. The architecture includes:

- A VPC with public and private subnets
- EC2 instances behind an Application Load Balancer (ALB)
- RDS (MySQL) instance in private subnet
- S3 bucket for static content and backups
- AWS Lambda function triggered on S3 uploads
- Auto Scaling for EC2 instances
- GitHub for version control

---

## 🗂️ Project Structure
.
├── terraform/ # Terraform IaC scripts (networking)
│ ├── main.tf
│ ├── security_groups.tf
│ ├── outputs.tf
│ └── variables.tf
├── cloudformation/ # CloudFormation templates
│ ├── ec2_stack.yaml
│ ├── rds_stack.yaml
│ └── lambda_s3_trigger.yaml
├── boto3/ # Boto3 Python scripts
│ ├── create_bucket_and_upload.py
│ ├── list_running_instances.py
│ ├── retrieve_instance_metadata.py
│ └── invoke_lambda.py
├── lambda/
│ └── lambda_log_s3_upload.py # Lambda function script
├── html/
│ └── index.html # Simple web page for EC2
├── architecture_diagram.png # Architecture diagram
├── README.md # Project documentation


---

## Prerequisites

- AWS CLI configured with IAM credentials
- Terraform v1.0+
- Python 3.x with `boto3` installed
- AWS account with access to EC2, VPC, RDS, Lambda, CloudFormation, S3, IAM

---

## Setup Instructions

### Step 1: Create Networking with Terraform

```bash
cd terraform/
terraform init
terraform apply -auto-approve

This creates:

    VPC, public and private subnets

    Internet Gateway, NAT Gateway

    Route tables, Security Groups

Step 2: Deploy Infrastructure with CloudFormation
cd ../cloudformation/

# Deploy EC2 stack
aws cloudformation deploy \
  --template-file ec2_stack.yaml \
  --stack-name EC2Stack \
  --capabilities CAPABILITY_NAMED_IAM

# Deploy RDS stack
aws cloudformation deploy \
  --template-file rds_stack.yaml \
  --stack-name RDSStack \
  --capabilities CAPABILITY_NAMED_IAM

# Deploy Lambda + S3 trigger
aws cloudformation deploy \
  --template-file lambda_s3_trigger.yaml \
  --stack-name LambdaS3Stack \
  --capabilities CAPABILITY_NAMED_IAM

Step 3: Upload HTML Page to EC2
scp html/index.html ec2-user@<EC2_PUBLIC_IP>:/var/www/html/index.html

Step 4: Upload File to S3 and Check Logs

    Upload a file to your S3 bucket (e.g., using Boto3 or AWS Console)

    Go to CloudWatch Logs and verify that the Lambda function logs the uploaded file’s name and bucket

Step 5: Run Python Scripts
cd ../boto3/
python create_bucket_and_upload.py
python retrieve_instance_metadata.py
python list_running_instances.py
python invoke_lambda.py

Verification

    Terraform: VPC and networking created

    EC2 and RDS: Deployed using CloudFormation

    Lambda: Logs S3 uploads to CloudWatch

    Web page: Served from EC2 instance

    Autoscaling: Enabled in EC2 stack

    Python Boto3 scripts: Functional for all tasks

