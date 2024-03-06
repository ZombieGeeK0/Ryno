# importamos las librerías necesarias
import socket, time
from colorama import Fore, Back

# hacemos los colores de colorama
GREEN = Fore.WHITE + Back.GREEN
RESET = Fore.RESET + Back.RESET

# creamos los argumentos de parser
parser = argparse.ArgumentParser()

parser.add_argument('--scan', '-s',
                    required=True,
                    help="Indica el host a escanear en busca de puertos abiertos")

args = parser.parse_args()

# asignamos el objetivo
target = args.scan

# inciamos el servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# se empieza el escaneo
target_ip = socket.gethostbyname(target)
print(f'{GREEN}[INFO]:{RESET} Starting scan on host:', target_ip)
 
# función para escanear puertos
def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
      
    except:
        return False
 
start = time.time()
 
# se escanean los puertos del 0 al 4
for port in range(5):
    if port_scan(port):
        print(f'port {port} is open')
    else:
        print(f'port {port} is closed')
 
end = time.time()
print(f'Time taken {end-start:.2f} seconds')
