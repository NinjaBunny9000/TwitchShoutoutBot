import os
from twitchio.ext import commands
from interface import twitch_api

from logger import loggymclogger as log

bot_name = os.environ['BOT_NICK']
team = twitch_api.team_members

# set up the bot
bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=bot_name,
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']] 
)


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
    if author.lower() == bot_name.lower() or author.lower() == os.environ['CHANNEL']:
        return

    # greet team members in the chat!
    global team
    for member in team:
        if author.lower() == member.lower():
            msg = f"📢 @{author} has arrived!!! They're a fellow stream-team member! \
                Learn more about the team here: https://www.twitch.tv/team/{os.environ['TEAM']}"
            await ctx.channel.send(msg)
            log.debug(f"TEAM MEMBER REGISTERED: {author}")
            team.remove(author)  # prevent being greeted more than once
            # TODO: also greets them via tts

bot.run()  # start the bot
