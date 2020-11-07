import os
import getpass

password=getpass.getpass("password : ")

if password != "12":
	print("Incorrect")
	exit()

while True :

	os.system("clear")

	print("""
	press 1 : to start the aws EC2 instance
	press 2 : to create the EBS volume
	press 3 : to attach the EBS volume to the EC2 instance	
	press 4 : to create the S3 Bucket
	press 5 : to copy file from your storage to S3 Bucket
	press 6 : to create Cloudfront Distribution
	press 7 : to exit
	""")

	ch = input("enter your choice : ")
	
	if ch == "1":
		inid = input("enter your EC2 instance id : ")
		os.system("aws ec2 start-instances --instance-ids {}".format(inid))
		print("Successfully started your Ec2 instance")
	
	elif ch == "2":
		reg = input("enter the A.Z name where you want to create EBS vol. : ")
		size = input("enter the size of EBS vol. you want to make : ")
		os.system("aws ec2 create-volume --availability-zone {} --size {}".format(reg,size))
		print("Successfully created your EBS vol. of size {}".format(size))
	
	elif ch == "3":
		volid = input("enter your EBS vol. id : ")
		os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/xvdf".format(volid,inid))
		print("Successfully attached your EBS to your Ec2 instance")

	elif ch == "4":
		buck = input("create your Unique Bucket name : ")
		buckreg = input("enter region where you want to make your Bucket : ")
		os.system("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(buck,buckreg,buckreg))
		print("Successfully created Bucket {} in {}".format(buck,buckreg))

	elif ch == "5":
		filep = input("enter the path of file : ")
		os.system("aws s3 cp {} s3://{}/{} --acl public-read".format(filep,buck,filep))
		print("Successfully copied the file from your storage to S3 bucket")

	elif ch == "6":
		buckn = input("enter your S3 bucket name you want to attach in cloudfront : ")
		os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(buckn))
		print("Successfully created cloudfront distribution")

	elif ch == "7":
		exit()
	
	else :
		print("incorrect choice")

	input("press enter to continue..")
