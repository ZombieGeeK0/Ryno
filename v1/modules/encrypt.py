# import the necesary libraries
import argparse
from colorama import Fore, Back

# create the colorama colors
GREEN = Fore.WHITE + Back.GREEN
RESET = Fore.RESET + Back.RESET

# create the parser arguments
parser = argparse.ArgumentParser()

parser.add_argument('--sca', '-s',
                    required=True,
                    help="Indicates host to be scanned for open ports")

args = parser.parse_args()
