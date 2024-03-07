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
                    required=True,
                    help="Indicates the encrypt algorithm to use")

parser.add_argument('--text', '-t',
                    required=True,
                    help="Indicates the text")

args = parser.parse_args()

passkey = "wow"
