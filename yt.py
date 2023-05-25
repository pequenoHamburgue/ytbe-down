import os
from pytube import YouTube

#url do video
video_url = input("URL: ")

#instancia para objeto youtube
video = YouTube(video_url)

#obtem o titulo do video
video_title= video.title

# define o nome de arqvo de saida

output_filename = f'{video_title}.mp4'

desktop_path = os.path.expanduser('~/Desktop')

output_path = os.path.join(desktop_path, output_filename)

streams = video.streams.filter(file_extension='mp4')

if len(streams) == 0:
    print("não foi possivel encontrar stram do video")
else:
    stream = streams.first()

    print(f"iniciando donwload {video_title}")
    stream.download(output_path=desktop_path, filename=output_filename)
    print("dowlad concluido")
