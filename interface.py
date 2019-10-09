import os
import requests
from utils.logger import loggymclogger as log

class TwitchInterface:
    """Interfaces with twitch API. Use this to call for a list of team members
    at the start of streams."""

    def __init__(self):
        """Set up the instance with the credentials and settings we need to
        access info via twitch's API"""
        self.base_url = "https://api.twitch.tv"
        self.header = {
            'Accept' : "application/vnd.twitchtv.v5+json",
            'Client-ID' : os.environ['CLIENT_ID']
        }
        self.team_members = self._get_team_members()

    def request(self, method, url, params=None, limit=None, version='kraken'):
        if method is 'GET':
            r = requests.get(f"{self.base_url}/{version}/{url}", headers=self.header)
            return r.json()

    def _get_team_members(self):
        'requests a list of team members (in lower) every time the bot starts'
        members = list()
        data = self.request(method='GET', url=f"teams/{os.environ['TEAM']}")
        for user in data['users']:
            members.append(user['name'])
        return members

    def _set_team_members(self):
        self.team_members = []
        self.team_members = self._get_team_members()
        log.debug(f"TEAM MEMBERS {self.team_members}")


twitch_api = TwitchInterface()

# TODO: set up a class hat handles making api calls for tts
class TTSInterface:
    """Interface with TTS providor (right now we're using StreamElements api calls)"""

    def __init__(self):
        pass


tts = TTSInterface()