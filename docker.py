import os
os.system("tput setaf 3")
print("     ---------------------------------------------------      ")
print("             Welcome to the Docker World !!!                  ")
print("     --------------------------------------------------       ")
os.system("tput setaf 7")
while True:
    os.system("tput setaf 4")
    print("Press 1: Install apache server")
    print("Press 2: Start apache server")
    print("Press 3: Status apache server")
    print("Press 4: Wrtie file ")
    os.system(" tput setaf 7")
    ch=int(input("Enter your choice:"))
    if ch==1:
        os.system("apt-get install apache2 -y")

    elif ch==2:
        os.system("service apache2 start")

    elif ch==3:
        os.system("service apache2 status")

    elif ch==4:
        os.system("tput setaf 3")
        n=input("Enter your file name:")
        os.system("tput setaf 7")
        os.system("vim {0}".format(n))
        os.system("chmod +x {0}".format(n))
        os.system("cp {0} /var/www/html".format(n))
