# importamos las librerías necesarias
import os, time, random, re, sys
from googlesearch import search
from colorama import Fore, Back

# creamos los argumentos de parser
parser = argparse.ArgumentParser()

parser.add_argument('--research', '-r',
                    required=True,
                    help="Indica el e-mail a buscar")

args = parser.parse_args()

# creamos la clase de colores
class color:
  GREEN = Fore.WHITE + Back.GREEN
  RESET = Fore.RESET + Back.RESET

# creamos la función principal
def main():
    email = args.research
    if email == "" or email == " ":
        print(f'\n{color.GREEN}[INFO]:{color.RESET} Error: Debes ingresar un email en el argumento')
        sys.exit()
  
    else:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
      
        if (re.fullmatch(regex, email)):
          
            print(f'\n{color.GREEN}[INFO]:{color.RESET} Email válido')
          
        else:
            print(f'\n{color.GREEN}[INFO]: {color.RESET}Email inválido')
            sys.exit()
          
    dom = ["com","com.tw","co.in","be","de","co.uk","co.ma","dz","ru","ca"]
    tld = random.choice(dom)
    command = f'intext:{email}'
    command2 = f"site:@ filetype:PDF intext:{email}"
    command3 = f"site:facebook.com intext:{email}"
    command4 = f"site:twitter.com intext:{email}"
    command5 = f"site:instagram.com intext:{email}"
  
    for j in search(command, tld, num=10, stop=10, pause=2):
        print(f'\n{color.GREEN}[INFO]:{color.RESET} Resultados encontrados: {j}')
      
    print(f'\n{color.GREEN}[INFO]:{color.RESET} Buscando email en archivos PDF...')
  
    time.sleep(3)
  
    for i in search(command2, tld, num=10, stop=10, pause=2):
        print(f'\nResultados encontrados!: {i}')
    print(f'\n{Colores.amarillo}[~] Buscando correo electronico en redes sociales...')
    for a in search(command3, tld, num=10, stop=10, pause=2):
        print(f'\nResultados encontrados!: {a}')
    for b in search(command4, tld, num=10, stop=10, pause=2):
      print(f'\nResultados encontrados!: {b}')
    for c in search(command5, tld, num=10, stop=10, pause=2):
      print(f'\nResultados encontrados!: {c}')
    print(f'\n{Colores.verde}[~] Iniciando socialscan...')
    time.sleep(3)
    print('')
    os.system(f"socialscan {email}")
    print(f'\n{Colores.azul}[~] Escaneo completo.')

main()
