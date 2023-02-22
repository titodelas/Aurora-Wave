import os
import wave
import argparse
import fade
from time import sleep
from rich.console import Console
from colorama import *

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='Select Audio File', dest='audiofile')
parser.add_argument('-m', help='Enter your Secret Message', dest='secretmsg')
parser.add_argument('-o', help='Your Output file path and name', dest='outputfile')
args = parser.parse_args()
af = args.audiofile
string = args.secretmsg
output = args.outputfile
arged = False
if af and string and output:
    arged = True
def cls():
  os.system("cls")
def help():
  print (f'''
  {Fore.GREEN}Extract Your Secret Message from Audio Wave File.\n\n
  {Fore.RESET}usage: Aurora_show.py [-h] [-f AUDIOFILE]
  optional arguments:
  -h, --help    {Fore.CYAN}show this help message and exit{Fore.RESET}
  -f AUDIOFILE  {Fore.CYAN}Select Audio File{Fore.RESET}
  -m SECRETMSG  {Fore.CYAN}Enter your message{Fore.RESET}
  -o OUTPUTFILE {Fore.CYAN}Your output file path and name{Fore.RESET}''')
  
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

def em_audio(af, string, output):
    if not arged:
      help()
    else:
      print(f"{Fore.YELLOW}[*] Please wait...")
      console = Console()
      tasks = [f"task {n}" for n in range(1, 8)]

      with console.status(f"{Fore.MAGENTA}Working on tasks...") as status:
          while tasks:
              task = tasks.pop(0)
              sleep(1)
              console.log(f"{task} complete")
      waveaudio = wave.open(af, mode='rb')
      frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
      string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
      bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
      for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
      frame_modified = bytes(frame_bytes)
      with wave.open(output, 'wb') as fd:
        fd.setparams(waveaudio.getparams())
        fd.writeframes(frame_modified)
      waveaudio.close()
      print (f"{Fore.GREEN}Done...{Fore.RESET}")
cls()
banner()
try:
  em_audio(af, string, output)
except:
  print(f"{Fore.RED}Something went wrong!! try again")
  quit('')