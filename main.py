import requests as req
from pprint import pprint as pp
iowa_teams = []
teams = req.get('https://theorangealliance.org/api/team/', headers={
    "Content-Type": "application/json",
    "X-TOA-Key": "96b204527e38d1826dce328bc44fb791c8da5376a74bca5b1ca2d3993c076e7f",
    "X-Application-Origin": "Delta Robotics TOA API Test"
})
json = teams.json()

for x in json:
    if "IA" in x['state_prov']:
        iowa_teams.append(x)

for x in iowa_teams:
    pp(x['team_name_short'])

