'''
©2024 By ZombieGeek0, MIT License (https://github.com/ZombieGeeK0/Ryno?tab=MIT-1-ov-file).
'''

# import the necesary libraries
import argparse, os
from colorama import Fore, Back

# create the colorama colors
GREEN = Fore.WHITE + Back.GREEN
RESET = Fore.RESET + Back.RESET

# create the parser arguments
parser = argparse.ArgumentParser()

parser.add_argument('--console', '-c',
                    required=False,
                    help="Requests an interactive shell")

parser.add_argument('--scan', '-s',
                    required=False,
                    help="Scan the ports of the IP indicated next to the argument")

parser.add_argument('--leave', '-l',
                    required=False,
                    help="Exits the terminal and/or program")

parser.add_argument('--text', '-t',
                    required=False,
                    help="Provides information of some kind in plain text")

parser.add_argument('--encrypt', '-e',
                    required=False,
                    help="Specifies the passkey with which to encrypt a string")

parser.add_argument('--unhash', '-u',
                    required=False,
                    help="Indicates the passkey to decrypt the text")

parser.add_argument('--research', '-r',
                    required=False,
                    help="Search for an email on OSINT pages")

parser.add_argument('--qrcode', '-q',
                    required=False,
                    help=" Generates a QR code of a given page after the argument '-q'")

parser.add_argument('--osint', '-o',
                    required=False,
                    help="Scan a web with OSINT techniques")

args = parser.parse_args()

if args.console:
  os.system('cd modules && python3 console.py')

elif args.scan:
  os.system('cd modules && python3 port_scanner.py')

elif args.leave:
  os.system('cd modules && python3 leave.py')

elif args.encrypt:
  os.system('cd modules && python3 encrypt.py')

elif args.unhash:
  os.system('cd modules && python3 decrypt.py')

elif args.research:
  os.system('cd modules && python3 email.py')

elif args.qrcode:
  os.system('cd modules && python3 qrcode.py')

elif args.osint:
  os.system('cd modules && python3 osint_web_scanner.py')

else:
  print(f'\n[{GREEN}INFO{RESET}]: Error: Check if you have added all the necessary arguments\n')
