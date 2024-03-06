# importamos las librerías necesarias
import os, sys, socket, argparse, requests, qrcode
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

def generate_qrcode(url,
              version=4,
              box_size=10,
              border=4,
              fill_color=(12, 52, 127),
              back_color=(187, 202, 229),
              name='qrcode_output.png'):
                
  qr = qrcode.QRCode(version=version,
                     error_correction=qrcode.constants.ERROR_CORRECT_L,
                     box_size=box_size,
                     border=border)
                
  # Adjuntamos el texto o url que se desea vincular
  qr.add_data(url)
  qr.make(fit=True)
                
  # Creamos la imagen del QR Code con colores RGB
  qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)
                
  # Guardamos el QR Code generado
  qr_img.save(name)

# definimos la vriable url
url = args.qrcode

# ejecutamos la función
generate_qrcode(url=url)
