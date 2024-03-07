# import the necesary libraries
import os, sys, argparse

# create the parser arguments
parser = argparse.ArgumentParser()

parser.add_argument('--leave', '-l',
                    required=False,
                    help="Indicates the time to exit the terminal")

args = parser.parse_args()

# close the terminal
os.system(f'sleep {args.leave} && clear && exit')
