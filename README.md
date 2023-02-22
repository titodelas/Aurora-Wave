
# Aurora Wave
> Embedding secret messages in wave audio file using steganography

![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/titodelas/Aurora-Wave?style=flat-square) ![Lines of code](https://img.shields.io/tokei/lines/github/titodelas/Aurora-Wave?style=flat-square) ![GitHub](https://img.shields.io/github/license/titodelas/Aurora-Wave?style=flat-square)

Aurora Wave is a python based program for simple audio steganography. You can hide your secret text messages in wave audio file. You can play this audio in any media player and secretly share your private message with anyone. The only difference you will notice is a small noise on the original audio, nothing very big, it will seam like you have a bad mic, or just bad audio.

<img src="https://i.imgur.com/gZoYIA1.png"  
alt="Aurora Wave Demo"  
style="float: center; margin-right: 10px;" />

## Installation
```sh
git clone https://github.com/titodelas/Aurora-Wave.git
cd Aurora-Wave
```

## Usage example
Aurora Wave have two python scripts.
-   **Aurora_hidden.py :**  for hiding secret information.
-   **Aurora_show.py :**  to extract secret information for wave audio file.

### Hide Secret Information in Audio file
```
python Aurora_hidden.py -f Demo.wav -m "Secret Msg" -o output.wav

```
### Extract Secret Information from Audio file
```
python Aurora_show.py -f output.wav
```