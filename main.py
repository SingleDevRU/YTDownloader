from pytube import YouTube

path = input("Введите URL: ")
yt = YouTube(path)

stream = yt.streams.filter(only_audio=True).get_by_itag(251)
stream.download("./Download")