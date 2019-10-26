[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y013678)

# Team Member Shoutout Bot for Twitch Streamers

This is a simple bot that does basic shotouts in twitch chat whenever team members hop in and say something. For now, alerts are chat-only. Next version (soon) will also include a TTS shoutout option.

This and other Twitch bots are being developed during [Live-Streams on Twitch](https://twitch.tv/ninjabunny9000).

## Getting Started

You can choose 2 methods to install:

- [Native](#native-installation) (Install & run python on your machine)
- [Docker](#docker-installation) (Install & run in an isolated docker container)

### Native Installation

Should be quick & easy to get up and running but, ofc, if you ever have questions about the specifics, please feel free to ask me during streams or post an issue above.

#### Prerequisites

- Download & install [Python 3.6](https://www.python.org/downloads/release/python-368/) (if you haven't already)
- Install PIPENV (venv + package manager) ⇒ `python -m pip install pipenv`
- oauth token & client-id for a Twitch account for your bot

#### Installing

1. Download & install Python (if you haven't already)
2. Clone the repo, unzip it somewhere
3. Open up a console window and navigate to the directory you unzipped it in
4. Install requirements via `pipenv install`
5. Copy & rename `.env-example` to `.env`
6. Pop in all your secrets into the respective areas within `.env`
7. Back to the console, do the `pipenv run python bot.py` thing to start the bot
8. The bot should greet chat when it comes online.

#### If you're having trouble starting the bot...

If using `pipenv run python bot.py` doesn't work, it might be how your environment variables are set up. Try these out...

- `python -m pipenv run python bot.py`
- `python3 -m pipenv run python3 bot.py`

If you're still having issues, let me (Bun) know.

### Docker Installation

#### One Prerequisite

You only need Docker Installed:

- [Docker for Mac](https://www.docker.com/products/docker-desktop)
- [Docker for Windows](https://www.docker.com/products/docker-desktop)

#### Installation

1. Clone this repo and change into the directory
1. Run `docker-compose build`

#### Running

1. Run `docker-compose up -d` to run in background
1. Run `docker-compose down` to bring down the service

#### All-in-one

1. Run `docker-compose up --build` to build and run the bot

## Customizing the greeting

You can customize the greeting on `line 43` in `bot.py`. Default, it looks like this:

> 📢 @{team_member} has arrived!!! They're a fellow stream-team member! Learn more about the team here: https://www.twitch.tv/team/{team_name}

## Events

There are 2 events that are used in the code right now.. `event_ready` and `on_event`.

You can find more info in [TwitchIO's official documentation](https://twitchio.readthedocs.io/en/rewrite/twitchio.html).

### event_ready

This executes when the bot comes online, and will print out to the console.

### event_message

This function executes once per event (or message) sent. You can make it handle input from chat that _aren't_ necesarily commands, and fun stuff like that.

## Progress & Development Info

### Contributors & Licenses

[NinjaBunny9000](https://github.com/NinjaBunny9000) - _Author, Project Manager_ - [Twitch](https://twitch.tv/ninjabunny9000) // [Twitter](https://twitter.com/ninjabunny9000)

### Special Thanks

Literally everyone that's helped even the smallest bit during streams. Thank you so much, y'all!
