# import the necesary libraries
import socket, time, argparse
from colorama import Fore, Back

# create the colorama colors
GREEN = Fore.WHITE + Back.GREEN
RESET = Fore.RESET + Back.RESET

# create the parser arguments
parser = argparse.ArgumentParser()

parser.add_argument('--scan', '-s',
                    required=False,
                    help="Indicates host to be scanned for open ports")

args = parser.parse_args()

# declare the target
target = args.scan

# start the socket server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# start the scanning
target_ip = socket.gethostbyname(target)
print(f'[{GREEN}INFO{RESET}]: Starting scan on host:', target_ip)
 
# function for the port scanning
def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
      
    except:
        return False
 
start = time.time()
 
# ports 0 to 4 are scanned
for port in range(5):
    if port_scan(port):
        print(f'[{GREEN}INFO{RESET}]: The port {port} is open')
    else:
        print(f'[{GREEN}INFO{RESET}]: The port {port} is closed')
 
end = time.time()
print(f'[{GREEN}INFO{RESET}]: Time taken: {end-start:.2f} seconds')
