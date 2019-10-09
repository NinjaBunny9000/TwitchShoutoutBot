from config import bot, settings
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
    
    elif token[1] == 'on':
        settings._set_sob(True)  # flip dat shiz on
        await ctx.send(f"Shoutouts reenabled. (is that a word or nah?)")

    elif token[1] == 'off':
        settings._set_sob(False)  # flip dat shiz off
        await ctx.send(f"Shoutouts temprarily disabled.")

    elif token[1] == 'state':
        if settings._get_sob():
            msg = f"@{ctx.author.name}, shoutouts are enabled."
        else:
            msg = f"@{ctx.author.name}, shoutouts are disabled."
        await ctx.send(msg)
    
    else: 
        return