# importamos las librerías necesarias
import requests, os, argparse, sys, socket
from colorama import Fore, Back

# creamos los argumentos de parser
parser = argparse.ArgumentParser()

parser.add_argument('--midi_number', '-n',
                    required=True,
                    help="número de nota MIDI")

parser.add_argument('--duration', '-d',
                    required=True,
                    help="duración en fracción de beat")

args = parser.parse_args()

# args.console

# hacemos los colores de colorama
GREEN = Fore.WHITE + Back.GREEN
RESET = Fore.RESET + Back.RESET

# hacemos la función principal
def main(url):
    response = requests.get(url)
 
    if response.status_code == 200:

        text = response.text

        print(text)

    else:
        print(f'\n{GREEN}[INFO]: {RESET}Error: El código de error de la página indicada no es válido.\n')

 

main('https://minelead.io')
