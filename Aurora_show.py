import os
import wave
import argparse
import fade
from time import sleep
from rich.console import Console
from colorama import *

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='audiofile', dest='audiofile')
args = parser.parse_args()
af = args.audiofile
arged = False
if af:
    arged = True


def cls():
    os.system("cls")


def help():
    print(f'''
  {Fore.GREEN}Extract Your Secret Message from Audio Wave File.\n\n
  {Fore.RESET}usage: Aurora_show.py [-h] [-f AUDIOFILE]
  optional arguments:
  -h, --help    {Fore.CYAN}show this help message and exit{Fore.RESET}
  -f AUDIOFILE  {Fore.CYAN}Select Audio File{Fore.RESET}''')


def banner():
    print(fade.purplepink("""
    
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


def ex_msg(af):
    if not arged:
        help()
    else:
        print(f"{Fore.YELLOW}[*] Please wait...")
        console = Console()
        tasks = [f"task {n}" for n in range(1, 5)]

        with console.status(f"{Fore.MAGENTA}Working on tasks...") as status:
            while tasks:
                task = tasks.pop(0)
                sleep(1)
                console.log(f"{task} complete")

        waveaudio = wave.open(af, mode='rb')
        frame_bytes = bytearray(
            list(waveaudio.readframes(waveaudio.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        string = "".join(chr(
            int("".join(map(str, extracted[i:i+8])), 2)) for i in range(0, len(extracted), 8))
        msg = string.split("###")[0]
        print(f"{Fore.GREEN}[+]Your Secret Message is: {Fore.RED}"+msg+""+Fore.RESET)
        waveaudio.close()


cls()
banner()
try:
    ex_msg(af)
except:
    print(f"{Fore.RED}Something went wrong!! try again")
    quit('')
