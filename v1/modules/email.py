# importamos las librerías necesarias
import requests, os, argparse, sys, socket
from colorama import Fore, Back

# creamos los argumentos de parser
parser = argparse.ArgumentParser()

parser.add_argument('--research', '-r',
                    required=True,
                    help="Indica el e-mail a buscar")

args = parser.parse_args()

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

# ejecutamos la función con el email indicado en el argumento
main(args.research)

# https://www.youtube.com/watch?v=2TyaTh1QRPw
