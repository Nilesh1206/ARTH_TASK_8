import os
import colored
from colored import stylize
print(stylize( """                ------------Welcome To Automation !!!!!-----------      """,colored.fg("yellow")))
print(stylize("""                 #####################################""",colored.fg("green")))
os.system("tput setaf 3")
print('                          \N{grinning face with smiling eyes}' + '\N{grinning face with smiling eyes} ')
os.system("tput setaf 7")
r=input(stylize("Would you like to login as ? (local/remote): ",colored.fg("red")))

if r=="local":

        print(""" \n
        Press 1 : date
        Press 2 : cal
        Press 3 : ip
        """)
        ch=int(input("Enter your Choice: "))
        print(ch)
        if ch==1:
            os.system("date")
        elif ch==2:
            os.system("cal")
        elif ch==3:
            os.system("ifconfig")
        else:
            os.system("time")

if r=="remote":
 ip=input(stylize("Enter host ip: ",colored.fg("cyan")))
 print(ip)
 def core():
     i=input(stylize("Please Enter master  ip :",colored.fg("cyan")))
     p=input(stylize("Please Enter master  port no : ",colored.fg("cyan")))
     print(i)
     print(p)
     os.system("echo \<configuration\> >> core-site.xml")
     os.system("echo \<property\> >> core-site.xml")
     os.system("echo \<name\>fs.default.name\<\/name\> >> core-site.xml")
     os.system("echo \<value\>hdfs://{0}:{1}\<\/value\> >> core-site.xml".format(i,p))
     os.system("echo \<\/property\> >> core-site.xml")
     os.system("echo \<\/configuration\> >> core-site.xml")

     os.system("scp core-site.xml {}:/etc/hadoop/core-site.xml".format(ip))
     os.system("rm -rf core-site.xml")

 def hdfs():
     d=input(stylize("Please Enter desired name of your directory:",colored.fg("pink_3")))
     print(d)
     os.system("ssh {} mkdir {}".format(ip,d))
     os.system("echo  \<configuration\> >> hdfs-site.xml")
     os.system("echo  \<property\> >> hdfs-site.xml")
     os.system("echo  \<name\>dfs.data.name\<\/name\> >> hdfs-site.xml")
     os.system("echo  \<value\>{}\<\/value\> >> hdfs-site.xml".format(d))
     os.system("echo  \<\/property\> >> hdfs-site.xml")
     os.system("echo  \<\/configuration\> >> hdfs-site.xml")
     os.system("scp hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ip))
     os.system("ssh {} hadoop datanode -format -y".format(ip))
     os.system("rm -rf hdfs-site.xml")



 while(True):

    os.system("tput setaf 3")
    print(""" \n
            Press 1 : date
            Press 2 : cal
            Press 3 : Installation of hadoop in datanode
            Press 4 : Configuration data node
            Press 5 : ip of datanode
            Press 6 : start namenode
            Press 7 : check namenode start or not
            Press 8 : start data node
            Press 9 : Check datanode is dtart or not
            Press 10 : Report
            Press 11 : Stop nameanode
            Press 12 : stop datanode
             """)
    os.system("tput setaf 7")
    ch=int(input(stylize("Enter your Choice: ",colored.fg("sea_green_2"))))
    print(ch)
    if ch==1:
          os.system("ssh {} date".format(ip))
    elif ch==2:
           os.system("ssh {} cal".format(ip))
    elif ch==3:
          os.system("ansible-playbook hadoop.yml")
    elif ch==4:
          core()
          hdfs()
    elif ch==5:
          os.system("ssh {} ifconfig".format(ip))
    elif  ch==6:
          os.system("hadoop-daemon.sh start namenode")
    elif ch==7:
          os.system("jps")
    elif ch==10:
          os.system(" ssh {} hadoop dfsadmin -report".format(ip))
    elif ch==9:
          os.system("ssh {} jps".format(ip))
    elif ch==8:
          os.system("ssh {} hadoop-daemon.sh start datanode".format(ip))
    elif ch==10:
          os.system("ssh {} hadoop-daemon.sh stop datanode".format(ip))
    elif ch==11:
          os.system("hadoop-daemon.sh stop namenode")
    elif ch==12:
          os.system("ssh {} hadoop-daemon.sh stop datanode".format(ip))
