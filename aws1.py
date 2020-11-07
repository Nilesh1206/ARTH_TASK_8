import os 
import colored 
from colored import stylize

print(stylize("-------------------------------------------------------------",colored.fg("green")))
print(stylize("            WEL-COME TO THE AWS WORLD                        ",colored.fg("yellow")))
print(stylize("-------------------------------------------------------------",colored.fg("green")))
while True:
   
   print("Press 1: Create IAM User")
   print("Press 2: Creating Security Group")
   print("Press 3: Create Key Pair")
   print("Press 4: \Launch Instance")
   print("Press 5: Create EBS Volume")
   print("Press 6: Attach Volume")
   
    
    
   ch=int(input(stylize("Enter your Choice: ",colored.fg("cyan"))))
   if  ch==1:
        i=input("Enter ther user name:")
        p=input("Please give power to user:")
        os.system("aws iam create-user --user-name {}".format(i))
        os.system("aws iam put-user-permissions-boundary --permissions-boundary arn:aws:iam::aws:policy/{0} --user-name {1}".format(p,i))
        
   elif ch==2:
        g=input("Enter the name of security group:")
        os.system('aws ec2 create-security-group --group-name {}  --description "my-security" --vpc-id vpc-f1697799'.format(g))
        s=input("Enter security group id:")
        p=input("Enter protocol name:")
        p1=input("Enter port number:")
        os.system("aws ec2 authorize-security-group-ingress --group-id {0}  --group-name {1} --protocol {2} --port {3} --cidr 0.0.0.0/0".format(s,g,p,p1))
        
   elif ch==3:
        k=input("Enter name of key:")
        os.system("aws ec2 create-key-pair --key-name {}".format(k))
       
   elif ch==4:
        i=input("Enter your aws image:")
        
        t=input("Enter the type of ec2-instance:")
        k=input("Enter name of key:")
        s1=input("Enter security group id:")
        n=input("Enter count to launch instances:")
        os.system("aws ec2 run-instances --image-id {0}  --instance-type {1} --key-name {2} --security-group-ids {3} --count {4}".format(i,t,k,s1,n))
       
       
   elif ch==5:
        s=input("Enter size of volume:")
        r=input("Enter region :")
        os.system("aws ec2 create-volume --volume-type gp2 --size {0} --availability-zone {1}".format(s,r))
        
   elif ch==6:
        vol=input("Enter volume id:")
        i=input("Enter instance-id:")
        d=input("Enter device type:")
        os.system("aws ec2 attach-volume --volume-id {0} --instance-id {1} --device {2}".format(vol,i,d))
       
