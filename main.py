import os
import re
import time
import sys

# Try importing requests, if not installed, install it automatically
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

def clear():
    os.system('clear')

def logo():
    print("""
\033[1;32m  ______ ____    ______ ______
\033[1;32m |  ____|  _ \  |  ____|  _  |
\033[1;32m | |__  | |_) | | |__  | |_) |
\033[1;32m |  __| |  _ <  |  __| |  _  |
\033[1;32m | |    | |_) | | |    | | \ \ 
\033[1;32m |_|    |____/  |_|    |_|  \_\ \033[1;36m [Created By : Karan Sharma]
\033[1;34m [Updated Fix : 2026 Headers]
\033[1;36m ========================================""")

def get_token():
    clear()
    logo()
    print("")
    
    # 1. Input Cookie
    try:
        cookie = input("\033[1;37m[?] Enter Facebook Cookie: \033[1;32m")
    except KeyboardInterrupt:
        print("\n\033[1;31mStopped by user.")
        return

    if not cookie:
        print("\033[1;31m[!] Error: Cookie cannot be empty!")
        return

    print("\n\033[1;36m[+] Fetching Token... Please wait...")

    # 2. Headers (Make FB think we are a real browser)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Cookie': cookie
    }

    # 3. Request to Ads Manager (Where token lives)
    try:
        url = "https://adsmanager.facebook.com/adsmanager/manage/campaigns"
        response = requests.get(url, headers=headers, allow_redirects=True)
        
        # 4. Search for Token using Regex
        # Looking for EAAB or EAAAA pattern
        token_search = re.search(r'(EAAB\w+)', response.text)
        
        if not token_search:
             # Try alternate pattern often found in 2026 source code
             token_search = re.search(r'(EAAAA\w+)', response.text)

        if token_search:
            token = token_search.group(1)
            print(f"\n\033[1;32m[SUCCESS] Token Generated Successfully!")
            print(f"\033[1;36m========================================")
            print(f"\033[1;33m{token}")
            print(f"\033[1;36m========================================")
            
            # Save to file
            with open('token.txt', 'w') as f:
                f.write(token)
            print("\033[1;32m[+] Token saved to token.txt")
        else:
            print("\n\033[1;31m[FAILED] Token not found in this cookie.")
            print("\033[1;37mReasons: Cookie expired / Account Locked / CP Checkpoint")

    except requests.exceptions.RequestException as e:
        print(f"\n\033[1;31m[ERROR] Network Issue: {e}")
    except Exception as e:
        print(f"\n\033[1;31m[ERROR] Script Error: {e}")

if __name__ == "__main__":
    get_token()
