# Ryno

`[INFO]` Image:

![Ryno](https://github.com/ZombieGeeK0/Ryno/assets/158185295/60c7052d-1f03-4a27-abf4-ec1b5a2214a0)

<hr>

`[INFO]` This software is developed for `Kali Linux` and made in Python.

`[INFO]` Support:

| System | Supported          |
| ------- | ------------------ |
| Windows   | :x: |
| Kali Linux   | :white_check_mark: |
| Debian   | :white_check_mark: |
| Red Hat   | :x: |
| Fedora | :x: |
| Android | :x: |
| MacOS | :x: |

<hr>

`[INFO]` Linux `installation:`

`[1]` Clone the `repository:`

    git clone https://github.com/ZombieGeeK0/Ryno
`[2]` Access to the `folder:`

    cd Ryno
`[3]` Give permissions to the `installer:`.

    chmod +x install.sh && chmod 777 install.sh

<hr>

`[INFO]` Arguments:

    [-c, --console]  Requests an interactive shell. It is accompanied by the time in which to open the console in seconds
    [-s, --scan]  Scan the ports of the IP indicated next to the argument
    [-e, --exit]  Exits the terminal and/or program
    [-t, --text]  Provides information of some kind in plain text   
    [-c, --cript]  Is followed by the name of the hash with which to encrypt the plaintext subsequently specified with the "-t" parameter
    [-u, --unhash]  Breaks the hash on the encryption cipher specified after the "-u" parameter. The hashed plaintext is indicated by the parameter "-t"
    [-d, --detect]  Detects the hash with which a text has been encrypted. The argument "-d" is accompanied by the encrypted text
    [-r, --research]  Search for an email on OSINT pages. The email is indicated after the "-r" parameter
    [-q, --qrcode]  Generates a QR code of a given page after the argument "-q"

<hr>

`[INFO]` Examples:

    python3 ryno.py -c 3
    python3 ryno.py -s 127.0.1.1
    python3 ryno.py -e 3
    python3 ryno.py -c md5 -t hello
    python3 ryno.py -u md5 -t 5d41402abc4b2a76b9719d911017c592
    python3 ryno.py -d 5d41402abc4b2a76b9719d911017c592
    python3 ryno.py -r iamdonald@gmail.com
    python3 ryno.py -q https://www.google.com

<hr>

páginas en las q se busca con OSINT email

decir los cifrados criptograficos soportados

Explicacion del funcionamiento

poner 📬 mailbox para cpontaxctp
imagen

contacto
