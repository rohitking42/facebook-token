import re
import os
import time

def clear():
    os.system('clear')

def logo():
    print("""
\033[1;32m  ______ ____    ______ ______
\033[1;32m |  ____|  _ \  |  ____|  _  |
\033[1;32m | |__  | |_) | | |__  | |_) |
\033[1;32m |  __| |  _ <  |  __| |  _ < 
\033[1;32m |_|    |_| \_\ |_|    |_| \_\
\033[1;33m [Created By : Karan Sharma]
\033[1;36m [Updated Fix : 2026 Headers]
========================================""")

def get_token():
    clear()
    logo()
    cookie = input("\n\033[1;37m[?] Enter Facebook Cookie: \033[1;32m")

    # High Quality Headers (Browser Ban kar jayega)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Cookie': cookie
    }

    print("\n\033[1;36m[+] Fetching Token... Please wait...")
    
    try:
        # Request to Ads Manager (Best for EAAAA Token)
        response = requests.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns', headers=headers)
        html = response.text

        # Regex to find Token
        token_search = re.search(r'(EAAB\w+)', html)
        
        if not token_search:
            token_search = re.search(r'(EAAAA\w+)', html)

        if token_search:
            token = token_search.group(1)
            print(f"\n\033[1;32m[SUCCESS] Token Generated:\n\033[1;37m{token}\n")
            
            # Save to file
            with open('token.txt', 'w') as f:
                f.write(token)
            print("\033[1;33m[+] Token saved in token.txt")
        else:
            # Check for Checkpoint/Lock
            if "checkpoint" in html or "login" in html:
                print("\n\033[1;31m[FAILED] Account Checkpoint pe chala gaya hai login verify karo.")
            else:
                print("\n\033[1;31m[FAILED] Cookie Expired or Invalid. Try extracting from Kiwi Browser.")
                
    except Exception as e:
        print(f"\n\033[1;31m[ERROR] Connection Error: {e}")

if __name__ == "__main__":
    get_token()
