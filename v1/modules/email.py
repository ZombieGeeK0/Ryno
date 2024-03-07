# import the necessary libraries
import os, time, random, re, sys
from googlesearch import search
from colorama import Fore, Back

# create the parser arguments
parser = argparse.ArgumentParser()

parser.add_argument('--research', '-r',
                    required=True,
                    help="Indicate the e-mail address to search")

args = parser.parse_args()

# create the color class
class color:
  GREEN = Fore.WHITE + Back.GREEN
  RESET = Fore.RESET + Back.RESET

# create the main function
def main():
    email = args.research
    if email == "" or email == " ":
        print(f'\n[{GREEN}INFO{RESET}]: Error: You must enter an email in the argument')
        sys.exit()
  
    else:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
      
        if (re.fullmatch(regex, email)):
          
            print(f'\n[{GREEN}INFO{RESET}]: Valid email')
          
        else:
            print(f'\n[{GREEN}INFO{RESET}]: Email no valid')
            sys.exit()
          
    dom = ["com","com.tw","co.in","be","de","co.uk","co.ma","dz","ru","ca"]
    tld = random.choice(dom)
    command = f'intext:{email}'
    command2 = f"site:@ filetype:PDF intext:{email}"
    command3 = f"site:facebook.com intext:{email}"
    command4 = f"site:twitter.com intext:{email}"
    command5 = f"site:instagram.com intext:{email}"
  
    for j in search(command, tld, num=10, stop=10, pause=2):
        print(f'\n[{GREEN}INFO{RESET}]: Results found: {j}')
      
    print(f'\n[{GREEN}INFO{RESET}]: Searching email in PDF archives...')
  
    time.sleep(1)
  
    for i in search(command2, tld, num=10, stop=10, pause=2):
        print(f'\n[{GREEN}INFO{RESET}]: Results found: {i}')
    print(f'\n[{GREEN}INFO{RESET}]: Searching email in social media...')
  
    for a in search(command3, tld, num=10, stop=10, pause=2):
        print(f'\n[{GREEN}INFO{RESET}]: Results found: {a}')
      
    for b in search(command4, tld, num=10, stop=10, pause=2):
      print(f'\n[{GREEN}INFO{RESET}]: Results found: {b}')
      
    for c in search(command5, tld, num=10, stop=10, pause=2):
      print(f'\n[{GREEN}INFO{RESET}]: Results found: {c}')
      
    print(f'\n[{GREEN}INFO{RESET}]: Initializing socialscan...')
  
    time.sleep(1)
  
    print('')
    os.system(f"socialscan {email}")
    print(f'\n[{GREEN}INFO{RESET}]: The scan is completed')

main()
