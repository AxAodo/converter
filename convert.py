import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'nocheckcertificate': True,
}

# replace with your youtube video URL
url = 'http://www.youtube.com/watch?v=BaW_jenozKc'

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
