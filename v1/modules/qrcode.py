# importamos las librerías necesarias
import os, sys, socket, argparse, requests
from colorama import Fore, Back

# hacemos los colores de colorama
GREEN = Fore.WHITE + Back.GREEN
RESET = Fore.RESET + Back.RESET

# creamos los argumentos de parser
parser = argparse.ArgumentParser()

parser.add_argument('--qrcode', '-q',
                    required=True,
                    help="Indica la página de la que hacer el código QR")

args = parser.parse_args()

