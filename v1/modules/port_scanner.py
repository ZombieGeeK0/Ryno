# importamos las librerías necesarias
import socket, time

# creamos los argumentos de parser
parser = argparse.ArgumentParser()

parser.add_argument('--scan', '-s',
                    required=True,
                    help="Indica el host a escanear en busca de puertos abiertos")

args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# asignamos el objetivo
target = args.argument
 
# next line gives us the ip address
# of the target
target_ip = socket.gethostbyname(target)
print('Starting scan on host:', target_ip)
 
# function for scanning ports
 
 
def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False
 
 
start = time.time()
 
# here we are scanning port 0 to 4
for port in range(5):
    if port_scan(port):
        print(f'port {port} is open')
    else:
        print(f'port {port} is closed')
 
end = time.time()
print(f'Time taken {end-start:.2f} seconds')
