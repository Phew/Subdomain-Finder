import requests
import os

from colorama import *
# LOLLOL CHARGE DID THIS IN A VC WHILE YOU WERE STRUGGILING
file = open("subdomains.txt")

content = file.read()

subdomains = content.splitlines()

def main():
    os.system('cls')
    print(f'''
╔╗╔╔═╗╔╗ ╦ ╦╦  ╔═╗
║║║║╣ ╠╩╗║ ║║  ╠═╣
╝╚╝╚═╝╚═╝╚═╝╩═╝╩ ╩
    
    
    ''')
    discovered_subdomains = []
    domain = input(str('URL: '))   
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            #print(f"{Fore.RED}[+]{Fore.WHITE} Connection Error")
            pass
        else:
            print(f"{Fore.GREEN}[+] {Fore.WHITE}Discovered subdomain:", url)
            discovered_subdomains.append(url)
            with open("discovered_subdomains.txt", "w") as f:
                for subdomain in discovered_subdomains:
                    print(subdomain, file=f)
            

main()