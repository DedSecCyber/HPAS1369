import os, sys, time
from time import sleep as timeout
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
os.system("clear")
os.system("figlet HPAS1369")
print "Author   : Zero Hacker TH"
print "Group    : DedSec CyberTeam TH"
print "Codename : KH-001             "
print "Version  : 1.1                "
print
print "           [01]> Brute Force              "
print "           [02]> DDos Attack              "
print "           [03]> NMap PortScanner         "
print "           [04]> Install Tools Hacking    "
print 
print " [00]> Exit "
print
A = raw_input("HPAS1369 ==>> ")

if A == "1" or A == "01":
  os.system("python2 brute.py")

elif A == "2" or A == "02":
    os.system("clear")
    os.system("figlet DDOS Attack")
    ip = raw_input("IP Address : ")
    port = raw_input("Port       : ")
    packet =raw_input("Packet     : ")
    os.system("python2 pntddos %s %s %s" % (ip, port, packet))

elif A == "3" or A == "03":
    os.system("clear")
    os.system("figlet NMap Scan")
    host = raw_input("Host : ")
    os.system("nmap %s" % (host))

elif A == "4" or A == "04":
    os.system("python2 lazymux.py")
    
elif A == "0" or A == "00":
    sys.exit()
    
else:
     print "\nERROR: Wrong Input"
     timeout(3)
     restart_program()
