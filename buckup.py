# from __future__ import unicode_literals
# import youtube_dl
# print("Please enter your video youtube link: ")
# link = input("");

# ydl_opts = {
#     'format': 'bestaudio/best',
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '320',
#     }],
#     'outtmpl': '~/downloads/%(title)s.%(ext)s',
# }

# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([link])