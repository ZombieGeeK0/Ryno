# import the necesary libraries
import qrcode, argparse
from colorama import Fore, Back

# create the colorama colors
GREEN = Fore.WHITE + Back.GREEN
RESET = Fore.RESET + Back.RESET

# create the parser arguments
parser = argparse.ArgumentParser()

parser.add_argument('--qrcode', '-q',
                    required=False,
                    help="Indica la página de la que hacer el código QR")

args = parser.parse_args()

# define the variable url
url = args.qrcode

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
                
  # attach the text or url you wish to link to
  qr.add_data(url)
  qr.make(fit=True)
                
  # create the QR Code image with RGB colours
  qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)
                
  # save the QR code
  qr_img.save(name)

# execute the function
generate_qrcode(url=url)
