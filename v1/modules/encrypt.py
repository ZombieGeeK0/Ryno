# import the necesary libraries
import argparse
from colorama import Fore, Back
from simplecrypt import encrypt, decrypt

# create the colorama colors
GREEN = Fore.WHITE + Back.GREEN
RESET = Fore.RESET + Back.RESET

# create the parser arguments
parser = argparse.ArgumentParser()

parser.add_argument('--encrypt', '-e',
                    required=False,
                    help="Indicates the passket to encrypt the text")

parser.add_argument('--text', '-t',
                    required=False,
                    help="Indicates the text")

args = parser.parse_args()

# create the passkey
passkey = args.encypt

# the text to encrypt
str1 = args.text

# encrypt the text
cipher = encrypt(passkey, str1)
print(f'\n[{GREEN}INFO{RESET}]: Encrypted text: {cipher}')
