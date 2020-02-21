import requests as req
from pprint import pprint as pp
import time
import json

iowa_teams = []
teams = req.get('https://theorangealliance.org/api/team/9925/events/1920', headers={
    "Content-Type": "application/json",
    "X-TOA-Key": "96b204527e38d1826dce328bc44fb791c8da5376a74bca5b1ca2d3993c076e7f",
    "X-Application-Origin": "Delta Robotics TOA API Test"
})
results = teams.json()
event_keys = []
match_participant_key = []
match_data = []
total_matches = []
team_matches = []
team_alliance = []
for x in results:
    event_keys.append(x['event_key'])

pp(event_keys)

for x in event_keys:
    event_matches = req.get('https://theorangealliance.org/api/event/' + x + '/matches', headers={
             "Content-Type": "application/json",
             "X-TOA-Key": "96b204527e38d1826dce328bc44fb791c8da5376a74bca5b1ca2d3993c076e7f",
             "X-Application-Origin": "Delta Robotics TOA API Test"
         })
    total_matches.append(event_matches.json())
pp(total_matches)
for x in range(0, len(total_matches)):
    for y in total_matches[x]:
        for z in y['participants']:
            if z['team_key'] == '9925':
                team_matches.append(z['match_key'])
                team_alliance.append(z['match_participant_key'][-2])


pp(team_matches)
pp(team_alliance)
