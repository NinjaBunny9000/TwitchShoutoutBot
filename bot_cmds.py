import os
from config import bot, settings
from utils.logger import loggymclogger as log
from interface import twitch_api

log.debug(f"{__name__} loaded.")

@bot.command(name='sob')
async def sob(ctx):
    '!sob <subcommand> <variabels can look like this or whatever>'

    # check permissions
    if 'moderator' in ctx.author.badges or 'broadcaster' in ctx.author.badges:
        msg_contents = ctx.content
        token = msg_contents.split(' ', 2)  # tokenize™

        try:

            if token[1] == 'reset':
                twitch_api.reset_shoutouts()
                await ctx.send(f"Shoutout lists reset! Holla holla")
            
            elif token[1] == 'on':
                settings._set_sob(True)  # flip dat shiz on
                await ctx.send(f"Shoutouts re-enabled.")

            elif token[1] == 'off':
                settings._set_sob(False)  # flip dat shiz off
                await ctx.send(f"Shoutouts temprarily disabled.")

            elif token[1] == 'state':
                if settings._get_sob():
                    msg = f"@{ctx.author.name}, shoutouts are enabled."
                else:
                    msg = f"@{ctx.author.name}, shoutouts are disabled."
                await ctx.send(msg)

        except IndexError:
            msg = f"@{ctx.author.name} try {os.environ['BOT_PREFIX']}sob <on, off, reset, or state>"
            await ctx.send(msg)