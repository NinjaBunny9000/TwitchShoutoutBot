import os
from twitchio.ext import commands


class Settings():

    def __init__(self):
        self.sob_state = True

    def _set_sob(self, state):
        self.sob_state = state

    def _get_sob(self):
        return self.sob_state


settings = Settings()

# set up the bot
bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']] 
)