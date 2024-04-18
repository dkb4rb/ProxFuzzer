import sys
import requests
from termcolor import colored
from pwn import log

def print_colored_banner():
    banner = """
\033[1;36m  _  (\033[1;31m(`-')    (`-')              (`-')                           (`-')      (`-')    
\033[1;36m   \-.(OO ) <-.(OO )       .->    (\033[1;31mOO\033[1;36m)_.->    <-.          .->     (\033[1;31mOO\033[1;36m).->   (\033[1;31mOO\033[1;36m).-> 
\033[1;36m  _.'    \ ,------,) (`-')----.  (\033[1;31m_| \033[1;36m\_)--.(`-')-----.,--.(,--.  ,(_/----.  ,(_/----.  
\033[1;36m  (_...--'' |   /`. ' (\033[1;31mOO\033[1;36m).-.  ' \  `.'  / (\033[1;31mOO\033[1;36m|(_\---'|  | |(\033[1;31m`-')|__,    |  |__,    |  
\033[1;36m  |  |_.' | |  |_.' | (\033[1;31m_)\033[1;36m | |  |  \    .')  / |  '--. |  | |(\033[1;31mOO\033[1;36m)  (_/   /    (_/   /   
\033[1;36m  |  .___.' |  .   .' \|  |)|  |  .'    \   \_)  .--' |  | | |  \ .'  .'_    .'  .'_   
\033[1;36m  |  |      |  |\  \   '  '-'  ' /  .'.  \   `|  |_)  \  '-'(_ .'|       |  |       |  
\033[1;36m  `--'      `--' '--'   `-----' `--'   '--'   `--'     `-----'   `-------'  `-------'  
    """
    print(banner)
    print("\n")
    print("\t\t\t\t"  + colored("developed from @Dkb4rb - ", "cyan") + colored("Juan Duque", "green"))
    print("\n")

def fuzz_url(url_ready):
    r = requests.get(url_ready)
    if r.status_code == 200:
        log.success("OK - 200 *******  {}".format(colored(url_ready, "green")))

def run_fuzz(url, wordlist):
    with open(wordlist, 'r') as f:
        for line in f:
            fuzz_url(url + line.strip())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <URL base> <ruta del wordlist>")
        sys.exit(1)

    base_url = sys.argv[1]
    wordlist_path = sys.argv[2]

    print_colored_banner()
    log.info("󰓾   Target: {}".format(colored(base_url, "light_red")))
    log.info("   Wordlist: {}".format(colored(wordlist_path, "cyan")))
    print("\n")
    run_fuzz(base_url, wordlist_path)
