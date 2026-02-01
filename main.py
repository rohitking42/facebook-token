import requests
import re
import os
import time

def clear():
    os.system('clear')

def logo():
    print("""
\033[1;32m  ______ ____    ______ ______  _  ________ _   _ 
 |  ____|  _ \  |  ____|  _ \ | |/ /  ___| \ | |
 | |__  | |_) | | |__  | |_) || ' /| |__ |  \| |
 |  __| |  _ <  |  __| |  _ < |  < |  __|| . ` |
 | |    | |_) | | |    | |_) || . \| |___| |\  |
 |_|    |____/  |_|    |____/ |_|\_\_____|_| \_|
                                                
 \033[1;36m[+] Created By : Karan Sharma
 \033[1;36m[+] Tool Type  : Cookie To Token Converter
 \033[1;37m===============================================
    """)

def get_token():
    clear()
    logo()
    cookie = input("\033[1;33m[?] Enter Facebook Cookie: \033[1;37m")
    
    if not cookie:
        print("\n\033[1;31m[!] Cookie cannot be empty!")
        return

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'Cookie': cookie
    }

    print("\n\033[1;36m[+] Fetching Token... Please wait...")
    
    try:
        # Requesting Ads Manager to get the token
        response = requests.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns', headers=headers)
        html = response.text
        
        # Regex to find EAAB token
        token_match = re.search(r'(EAAB\w+)', html)
        
        if token_match:
            token = token_match.group(1)
            print(f"\n\033[1;32m[SUCCESS] Token Generated:\n")
            print(f"\033[1;37m{token}")
            
            # Save to file
            with open('token.txt', 'w') as f:
                f.write(token)
            print(f"\n\033[1;33m[+] Token saved to token.txt")
        else:
            print("\n\033[1;31m[FAILED] Cookie Invalid or Expired. Try a fresh cookie.")
            
    except Exception as e:
        print(f"\n\033[1;31m[ERROR] Connection Failed: {e}")

if __name__ == "__main__":
    get_token()
