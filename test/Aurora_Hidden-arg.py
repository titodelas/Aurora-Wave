import os
import wave
import argparse
from time import sleep
from fade import purplepink

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='Select Audio File', dest='audiofile')
parser.add_argument('-m', help='Enter your Secret Message', dest='secretmsg')
parser.add_argument('-o', help='Your Output file path and name', dest='outputfile')
args = parser.parse_args()

audio_file = args.audiofile
secret_msg = args.secretmsg
output_file = args.outputfile

arged = False
if audio_file and secret_msg and output_file:
    arged = True


def clear_screen():
    os.system("cls")


def show_help():
    print(f'''
    Extract Your Secret Message from Audio Wave File.
    
    usage: {__file__} [-h] [-f AUDIOFILE]
    optional arguments:
    -h, --help    show this help message and exit
    -f AUDIOFILE  Select Audio File
    -m SECRETMSG  Enter your message
    -o OUTPUTFILE Your output file path and name
    ''')


def show_banner():
    print(purplepink("""
     █████╗ ██╗   ██╗██████╗  ██████╗ ██████╗  █████╗ 
    ██╔══██╗██║   ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗
    ███████║██║   ██║██████╔╝██║   ██║██████╔╝███████║
    ██╔══██║██║   ██║██╔══██╗██║   ██║██╔══██╗██╔══██║
    ██║  ██║╚██████╔╝██║  ██║╚██████╔╝██║  ██║██║  ██║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

    [>] v1.0 www.delaas.xyz
    [>] Visit for more projects: github.com/titodelas
    [>] Hide your text message in wave audio file like MR.ROBOT
    """))


def embed_audio_message(audio_file, secret_msg, output_file):
    if not arged:
        show_help()
        return
    print("[*] Please wait...")
