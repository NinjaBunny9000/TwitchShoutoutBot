from config import bot
from utils.logger import loggymclogger as log
from interface import twitch_api

log.debug(f"{__name__} loaded.")

@bot.command(name='sob')
async def sob(ctx):
    '!sob <subcommand> <variabels can look like this or whatever>'

    msg_contents = ctx.content
    token = msg_contents.split(' ', 2)  # tokenize™
    
    if token[1] == 'refresh':
        # dor efreshy things
        twitch_api._set_team_members()
        await ctx.send(f"Shoutout lists refreshed! Holla holla")
    
    else: 
        return
