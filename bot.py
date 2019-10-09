import os
from config import bot, settings
from utils.logger import loggymclogger as log
from interface import twitch_api

bot_name = os.environ['BOT_NICK']
# team = twitch_api.team_members

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

    if settings._get_sob():
        # greet team members in the chat!
        for member in twitch_api.team_members:
            if author.lower() == member.lower() and author.lower() != os.environ['CHANNEL']:
                msg = f"📢 @{author} has arrived!!! They're a fellow stream-team member! \
                    Learn more about the team here: https://www.twitch.tv/team/{os.environ['TEAM']}"
                await ctx.channel.send(msg)
                log.debug(f"TEAM MEMBER REGISTERED: {author}")
                twitch_api.team_members.remove(author)  # prevent being greeted more than once
                # TODO: also greets them via tts


if __name__ == "__main__":
    bot.run()  # start the bot
