from colorama import Fore, Back, Style
from time import sleep
from pyfiglet import figlet_format
from os import system, sys
import datetime 
import random
system("clear")
green="\033[1;92m"
red ="\033[1;91m"
blue="\033[1;94m"
pink="\033[1;95m"
yellow="\033[1;93m"
white="\033[1;00m"
OF = "\033[0m"
ww = "\033[0;100m"
system("pip install colorama")
system("pip install pyfiglet")
system("clear")

h = (f"""{green}----0%
-------10%
----------20%
-------------30%
----------------40%
-------------------50%
----------------------60%
--------------------------70%
------------------------------80%
---------------------------------90%
------------------------------------100%""")
for i in h:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.01)


sleep(3)

system("clear")


print(Fore.RED+f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠶⠶⠶⠶⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣠⡴⠞⠛⠉⠉⣩⣍⠉⠉⠛⠳⢦⣄⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⣴⡿⣧⣀⠀⢀⣠⡴⠋⠙⢷⣄⡀⠀⣀⣼⢿⣦⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡾⠋⣷⠈⠉⠉⠉⠉⠀⠀⠀⠀⠉⠉⠋⠉⠁⣼⠙⢷⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣹⣆⠀⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠀⣰⣏⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠞⠋⠁⠙⢷⣄⠙⢷⣀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢀⡾⠋⠈⠙⠻⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠹⢦⡀⠙⠳⠶⢤⡤⠶⠞⠋⢀⡴⠟⠀⠀⠀⠀⠀⠀⠙⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⢀⣤⣤⣤⣤⣤⣤⣤⣿⣦⣤⣤⣤⣤⣤⣤⣴⣿⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢠⣴⠞⠛⠛⠻⢦⡄⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣿⣿⢶⣄⣠⡶⣦⣿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⢻⣿⠶⠟⠻⠶⢿⡿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢾⣄⣹⣦⣀⣀⣴⢟⣠⡶⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣭⣭⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠋⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣄⣀⠀⠀⢀⣤⣼⣧⣤⣤⣤⣤⣤⣿⣭⣤⣤⣤⣤⣤⣤⣭⣿⣤⣤⣤⣤⣤⣼⣿⣤⣄⠀⠀⣀⣠⡾⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠻⢧⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠼⠟⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ Amir ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    """)

print("")
print("")
print("")
print("")
sleep(0.9)

w = (f""" 
{blue} ~~~> hello im amir bazmandeh
{yellow} ~~~~> welcome to mo script
{pink} ~~~~~> my telegram id : @Pir_ostad
""")
for e in w:
    sys.stdout.write(e)
    sys.stdout.flush()
    sleep(0.08)

print("")
print("")
print("")
print("")
sleep(0.3)
r = print(figlet_format("Wait"))
sleep(4)

Dxprit = ["http://dxprit-hack-yftt15k-filter-supportbot-fil.phpnet.us/x.photo.htm", "http://B2n.ir/dxprit.sxs-support.bot"]
Virus = ["http://Hackweb.xyz/python.html.cs", "http://ffmodmenu.page.link/Anti-V", "https://linuxsecurity.expert/security-tools/linux-malware-detection-tools", "https://liveweave.com/JUcnd7"]
Bug_spam = ["https://Spam.SupportBot.rubika.ir/spam$%spam-/¥fttk-8085-python.bUg-/ping-error+106.404.151-/Error:-:404:-:rubika.ir-/H.N.Z.7H9/0.9.0.9.09.0.9.0.9.0.9.0.9.0.9.0.9.0.9.0.9.0.9*(Spam%100%)*yftt15k/-17k/-18k/yttf20k/am.am.am.am.am.am", "https://web.rubika.ir.spam.user.spam/yftt13k.yftt18k.yftt17k.yftt20k.yftt_07k.V.3.4.3.yftt30k.yftt15-/*(Spam)*supporbot.spam/0.11.11.C4.12.12-/0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.11.11.C4.12.12/5.106.8.15.spam.in.rubika/%100%Spam100", "https://spam.ir/CT.5.106.8.151.ip.server/反伊斯兰的/yft.1.0.1.0.3.4.3.5.1.0.1.0.3.4.3.4.Filtering_rubika.ir.3.5.2.0.8.1.3.7.6.9.1.9.8.7.4.1.1.4.0.viru3/spam-000-account.cyberpolice.ir"]
Bug_sexi = ["https://sex.com.filterig.sexi.in.rubika/0×C4,0×100,0.deviantart-bug-0000.4-php-YftTkS-112334/0.9.0.9.0.9.0-yftt15k-17k-18k-yttf20k-Filter-yftt17k.6.2.4.8.1.1.9.5.0.4.4.5.5.4.2.8.6./10.10.34.35-9999999.C400/af.af.f.af.af.af.af.afo", "https://sexbebin.com/5.5.1.3.9.1.5.6.2.3.7.6/5.106.8.151/f//i//l//t//e//r/5.1.4.3.1.0.4.9.9.3.5.6.1.7.4.3.1.0.4.9.9.3.5.6.1(@SupportBot)3.5.2.1.4.5.2.1.5.7.2.1.4.7.2.1.1.5.2.1", "https://sexbebin.com/BuG.in.rubika/RubikaSupportReport-bug-3.5.4-server-5.2.1.6.8.1.5.1.5.5.1.2.4.0.3.4.X.0.XX.0.x.Fil/yftt15k/-17k/-18k/-yttf20k/2.6.0.4.2.7.4.1.6.7.1.1.1.3.1.7.2.3.7.4.5.2.5.3.5.3.1.2.3.2.6.9.4.3.7.5.4.9"]
phishing = ["https://ipfs.eth.aragon.network/ipfs/bafybeicli5rykqzju75bhact3z3xwhmdvx537w5jpllw56ja3jp7nthocy/nnooddvneng.html", "https://en.m.wikipedia.org/wiki/Phishing", "https://support.microsoft.com/en-us/windows/protect-yourself-from-phishing-0c7ea947-ba98-3bd9-7184-430e1f860a44"]
hack_rubika = ["https://github.com/shahzadehack/AT-Dscript-Hack-filtering-account-rubika-hacker-cyber/blob/main/index.html", "https://hamyargps.com/blog/remote-rubika-hack"]

t = input(Fore.LIGHTCYAN_EX+f"""
(1) Dxprit
(2) Virus
(3) Bug spam
(4) Bug sexi
(5) phishing
(6) hack rubika
Please Enter The Number ==> : """)



if t == "1":
    print("")
    print("")
    print("")  
    print("")
    sleep(2)
    print(Fore.YELLOW+random.choice(Dxprit))
    print("")
    print("")
    print("")  
    print("")
    sleep(0.6)
    print(Fore.RED+"Bye")

if t == "2":
    print("")
    print("")
    print("")  
    print("")
    sleep(2)
    print(Fore.YELLOW+random.choice(Virus))
    print("")
    print("")
    print("")  
    print("")
    sleep(0.6)
    print(Fore.RED+"Bye")

if t == "3":
    print("")
    print("")
    print("")  
    print("")
    sleep(2)
    print(Fore.YELLOW+random.choice(Bug_spam))
    print("")
    print("")
    print("")  
    print("")
    sleep(0.6)
    print(Fore.RED+"Bye")

if t == "4":
    print("")
    print("")
    print("")  
    print("")
    sleep(2)
    print(Fore.YELLOW+random.choice(Bug_sexi))
    print("")
    print("")
    print("")  
    print("")
    sleep(0.6)
    print(Fore.RED+"Bye")

if t == "5":
    print("")
    print("")
    print("")  
    print("")
    sleep(2)
    print(Fore.YELLOW+random.choice(phishing))
    print("")
    print("")
    print("")  
    print("")
    sleep(0.6)
    print(Fore.RED+"Bye")

if t == "6":
    print("")
    print("")
    print("")  
    print("")
    sleep(2)
    print(Fore.YELLOW+random.choice(hack_rubika))
    print("")
    print("")
    print("")  
    print("")
    sleep(0.6)
    print(Fore.RED+"Bye")