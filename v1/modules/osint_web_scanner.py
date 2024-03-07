# import the necessary libraries
import requests, argparse, sys
from colorama import Fore, Back

# create the parser arguments
parser = argparse.ArgumentParser()

parser.add_argument('--osint', '-o',
                    required=True,
                    help="Indica la web a la que hacer las requests")

parser.add_argument('--text', '-t',
                    required=True,
                    help="Indica el nombre de usuario a buscar")

args = parser.parse_args()

# create the colorama colors
GREEN = Fore.WHITE + Back.GREEN
RESET = Fore.RESET + Back.RESET

# create the main function
def main(url):
    response = requests.get(url)
 
    if response.status_code == 200:
        plain_text = response.text
      
        if args.text in plain_text:
          print(f'\n[{GREEN}INFO{RESET}]: Username {args.text} is found')

        if args.text == '' or ' ':
          print(f'\n[{GREEN}INFO{RESET}]: Error: A user name must be entered\n')
          sys.exit()

        else:
          print(f'\n[{GREEN}INFO{RESET}]: Username {args.text} not found\n')
          sys.exit()

    else:
        print(f'\n[{GREEN}INFO{RESET}]: Error: The error code of the indicated page is invalid\n')
        sys.exit()

# execute the function with the email indicated in the argument
main(args.osint)
