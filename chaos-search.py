#!/usr/bin/env python3

import json
from os import system,mkdir,path
from sys import argv
from time import sleep

def banner():
    print("\n\033[92m"+"______#######__##___##__####______########__#######___________________________")
    print("_____##_______##___##__##_##_____##____##__##_________________________________")
    print("____##_______#######__######____##____##__#######_____________________________")
    print("___##_______##___##__##___##___##____##_______##______________________________")
    print("__#######__##___##__##____##__########__#######_______________________________")
    print("______________________________________________________________________________")
    print("_____________________#######__#######__####______#######__#######__##___##____")
    print("____________________##_______##_______##_##_____##___##__##_______##___##_____")
    print("___________________#######__#######__######____#######__##_______#######______")
    print("_______________________##__##_______##___##___##__##___##_______##___##_______")
    print("_________________#######__#######__##____##__##___##__#######__##___##________")
    print("\033[96m"+"                                                          Twiter: 0xNoobie1100"+"\033[0m\n")

def search(key,raw):
    for i in range(len(raw)):
        if raw[i]['name'].lower()==key.lower():
            print('found')
            print('\tNumber of subdomains => '+str(raw[i]['count'])+'\n\tName => '+raw[i]['name']+'\n\tUrl => '+raw[i]['program_url']+'\n\tPlatform => '+raw[i]['platform'])
            return raw[i]

def save_in_txt(found):
    print(found['URL'])
    direc='./chaos/'+found['name'].lower()
    mkdir(direc)
    system('wget -P ' + direc + '/ ' + found['URL'])
    file_name = found['URL'].split('/')[len(found['URL'].split('/'))-1]
    system('unzip ' + direc + '/' + file_name + ' -d ' + direc)

def clean_mess(direc):
    system("rm -rf ./chaos/" + direc + "/*zip ../index.json")

def main():
    banner()
    if not path.exists('./chaos'):
        mkdir('./chaos')
    if not path.exists('./chaos/index.json'):
        system("wget -P ./chaos/ 'https://chaos-data.projectdiscovery.io/index.json'")
    f = open('./chaos/index.json')
    raw = json.load(f)
    for i in range(len(argv)):
        if i!=0:
           found = search(argv[i],raw)
           if type(found)==dict:
               print('\nSaving subdomains for ' + argv[i])  
               save_in_txt(found)
               sleep(5)
               clean_mess(found['name'].lower())
           else:
                print('\033[31m' + '\n[+][+]No bounty program with the name ' + argv[i]+'\n' + '\033[0m')
    f.close()

if __name__ == "__main__":
    main()
