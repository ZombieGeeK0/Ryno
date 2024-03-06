# importamos las librerías necesarias
import requests, argparse, sys
from colorama import Fore, Back

# creamos los argumentos de parser
parser = argparse.ArgumentParser()

parser.add_argument('--osint', '-o',
                    required=True,
                    help="Indica la web a la que hacer las requests")

parser.add_argument('--text', '-t',
                    required=True,
                    help="Indica el nombre de usuario a buscar")

args = parser.parse_args()

# hacemos los colores de colorama
GREEN = Fore.WHITE + Back.GREEN
RESET = Fore.RESET + Back.RESET

# hacemos la función principal
def main(url):
    response = requests.get(url)
 
    if response.status_code == 200:
        plain_text = response.text
        # print(text)
      
        if args.text in plain_text:
          print(f'{GREEN}[INFO]:{RESET} Nombre de usuario {args.text} ha sido encontrado')

    else:
        print(f'\n{GREEN}[INFO]:{RESET} Error: El código de error de la página indicada no es válido.\n')
        sys.exit()

# ejecutamos la función con el email indicado en el argumento
main(args.osint)
