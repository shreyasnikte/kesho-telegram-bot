import urllib.request
import pafy
import vlc
from bs4 import BeautifulSoup
from time import sleep
import utils


def yt(text):

    try:
        textToSearch = text
        query = urllib.parse.quote(textToSearch)
        url_query = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url_query)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        vids = soup.find(attrs={'class':'yt-uix-tile-link'})
        # print(vids)
        url_video = 'https://www.youtube.com' + vids['href']
        video = pafy.new(url_video)
        best = video.getbest()
        playurl = best.url
        # print(playurl)


        # Over here playurl is best URL to play. Then we use VLC to play it.
        Instance = vlc.Instance("--no-video --aout=alsa")
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.play()
        # sleep(5)
        return player, vids['title']



    except Exception(e): print (e)

# while True:
#     pass

utils.init()
