import os
from config import bot, settings
from utils.logger import loggymclogger as log
from interface import twitch_api as twitch

bot_name = os.environ['BOT_NICK']

log.debug(f"{__name__} loaded.")

import bot_cmds

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    log.info(f"{bot_name} is online!")
    msg = f"/me has landed!"
    ws = bot._ws  # set up websocket for sending first message (no ctx yet)
    await ws.send_privmsg(os.environ['CHANNEL'], msg)


@bot.event
async def event_message(ctx):
    'everythign that happens in this function happens every time a message is sent in teh channel'

    author = ctx.author.name  # define the author of the msg

    # make sure the bot ignores itself and the streamer
    if author.lower() == bot_name.lower():
        return

    await bot.handle_commands(ctx)

    ### SHOUTOUTS AND STUFFS ###

    if settings._get_sob():

        # greet team members!
        for member in twitch.team_members:
            if author.lower() == member.lower() and author.lower() != os.environ['CHANNEL']:
                msg = f"📢 @{author} has arrived!!! They're a fellow stream-team member! \
                    Learn more about the team here: https://www.twitch.tv/team/{os.environ['TEAM']}"
                await ctx.channel.send(msg)
                log.debug(f"TEAM MEMBER REGISTERED: {author}")
                twitch.team_members.remove(author)  # prevent being greeted more than once
                # TODO: also greets them via tts

        # greet subscribers!
        if 'subscriber' in ctx.author.badges and author not in twitch.greeted_subs and author != os.environ['CHANNEL']: 
            months_subbed = int(ctx.author.tags['badge-info'].split('/')[1])

            # customize the following lines for custom greetings (based on subs)
            greetings = [
                (24, f"📣 @{author} has arrived! They've been supporting for [{months_subbed}] flippin months! "),
                (12,f"📣 @{author} is BACK! Thanks for the continued support of [{months_subbed}] months!"),
                (9, f"📣 @{author} had landed! Congrats on the sub babby 👶 and the support of [{months_subbed}] months!"),
                (6, f"📣 @{author} has arrived! Thanks for the [{months_subbed}] months support!"),
                (3, f"📣 @{author} is here! Welcome back! ([{months_subbed}] months of support)"),
            ]

            for month, message in greetings:
                if months_subbed >= month:
                    await ctx.channel.send(message)
                    break
            
            twitch.mark_as_greeted(author)


if __name__ == "__main__":
    bot.run()  # start the bot
