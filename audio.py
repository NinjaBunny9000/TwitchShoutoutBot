import pygame
import urllib3, shutil

# create an audio player thingy
class Audio:
    'handles audio for text-to-speech'

    def __init__(self):
        pygame.mixer.init()
        self.count = 1

    # method that plays audio files
    def play(self, file_name):
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()

    # create a method to handle tts
    def speak(self, text):
        'plays text-to-speed™ (the game)'
        url = f"https://api.streamelements.com/kappa/v2/speech?voice=Salli&text={text}"
        ctx = urllib3.PoolManager()
        file_name = f"static/tts{self.count%2}.mp3"  # double-buffering (hacky but hey it works)
        self.count += 1
        pygame.mixer.music.stop()
        with ctx.request('GET', url, preload_content=False) as res:
            with open(file_name, 'wb') as out_file:
                shutil.copyfileobj(res, out_file)
        self.play(file_name)

player = Audio()