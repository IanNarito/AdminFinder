import os
import requests
import argparse
import time
import random
from urllib.parse import urljoin
from utils import get_random_user_agent
from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
    banner = f"""{Fore.MAGENTA}
 █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
███████║██║  ██║██╔████╔██║██║██╔██╗ ██║    █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║    ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    """
    print(banner)
    print(f"{Fore.CYAN} Admin Panel Finder v1.0")
    print(f"{Fore.CYAN} Scans for common admin login paths.\n")

def scan_admin_panels(target_url, wordlist_path):
    try:
        with open(wordlist_path, "r") as f:
            paths = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}[!] Wordlist not found: {wordlist_path}")
        return

    print(f"{Fore.YELLOW}[+] Target: {target_url}")
    print(f"{Fore.YELLOW}[+] Total paths to check: {len(paths)}\n")

    headers = {
        "User-Agent": get_random_user_agent()
    }

    try:
        for path in paths:
            full_url = urljoin(target_url, path)
            try:
                response = requests.get(full_url, headers=headers, timeout=5)
                status = response.status_code

                if status in [200, 301, 302]:
                    print(f"{Fore.GREEN}[FOUND] {full_url} - Status: {status}")
                else:
                    print(f"{Fore.RED}[MISS] {full_url} - Status: {status}")

                time.sleep(0.1)

            except requests.RequestException:
                print(f"{Fore.MAGENTA}[ERROR] Could not connect to {full_url}")
                continue

    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}[!] Scan interrupted by user. Exiting gracefully. Byeee 👋")
        exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Admin Panel Finder")
    parser.add_argument("--url", required=True, help="Target website URL (e.g. http://example.com)")
    parser.add_argument("--wordlist", required=False, help="Path to wordlist file")

    args = parser.parse_args()
    wordlist_path = args.wordlist or os.path.join("wordlists", "common.txt")

    print_banner()
    scan_admin_panels(args.url, wordlist_path)
