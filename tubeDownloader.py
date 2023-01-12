from pytube import YouTube
from sys import argv
#argv da acesso à linha de comando, sendo um VETOR de string. Cada string deste vetor é um dos parâmetros da linha de COMANDO.

link = argv[1]
#criando um ytObj do link.
yt = YouTube(link)

print("Title: ", yt.title)

yd = yt.streams.get_highest_resolution()

print('Downloading...')

yd.download('C:/Users/FDTEC/Videos')

print(yd)

print('Downloading completed!!')