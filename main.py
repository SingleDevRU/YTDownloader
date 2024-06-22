from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=m2Ci5PT9rMk")

stream = yt.streams.filter(only_audio=True).get_by_itag(251)
stream.download("./Download")