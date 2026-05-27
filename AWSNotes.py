# EC2 instance set up in VPC
Requirements
Within AWS Account:
create VPC:
 -create subnets public and private(Isolated group of IP addresses within VPC)
 -assign cidr
 -create route tables for public and private (to route internal and externall traffice)
 -createinternet gateway-(created in public subnet that anyone can access ec2 instance)
 -create NAT gateway - to get only to private instance for internet 
  attach internet gateway VPC
 -in route table need to do subnet association for private and public subnets
 -in route table edit route where in public we have to add internet gateway and in private NAT gateway
 -after all vpc configuration we will setup EC2 instance in pubilc and private subnets and also give proper access
 via security groups
 - after connecting  public EC2 it should acccessible for all and private should as its in private 
 subnet.
 -this is where we can use secure isolated envt for servers or instances.

# todays topic - Auto scaling group
- for maximum availability
- cost saving 
-steps to create Auto scaling group
- craete a VPC
= crate subnets 
-create IGW
- create route table and do subnet associationa and edit route to IGW
 -create Terget group to target EC2
 create load balancer and attach to target group 
 -creat Auto scaling group and also create a launch template
 -define min  max and desire resouces to use
 min- minimum range of downscale,desired-maintain,max-maximum range for upscale
 -In ASG we can check health of resources 

# security Groups
-define inbound/outbound rule at instance level
-allowing particular traffice
# EBS Volume
-commands lsblk to check volume df -u
-add volume using aws console
-we can attach it to the EC2 instance
-we can also take snapshot of EBS volume  
-snapshot is kind of backup

#Real DevOps Usage

Snapshots used for:

Disaster recovery
Backup before deployment
Database recovery
Server migration
# IAM (Identity and Access Management )
-IAM User - Individual 
-IAM role - temporary permission and 
-IAM Groups - A collection of user where we can assign roles and permission 
-IAM Policy - Rule of permission or we can create custom policies for perticular AWS resources