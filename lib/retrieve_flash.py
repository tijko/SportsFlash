#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import collections
from parse_response import *

apikey = ""

CITIES = ['Boston', 'Chicago', 'Dallas', 'Los-angeles', 'New-york']
SPORTS = {'Baseball':'mlb', 'Basketball':'nba', 'Football':'nfl', 'Hockey':'nhl'}

def city():
    print '\nSelect a city:'
    for city in enumerate(CITIES, 1):
        print '    [%d] %s' % (city[0], city[1])
    choice = raw_input('> ')
    try:
        if not any(i==int(choice) for i in range(1, 6)):
            print '~Bad Selection!\n'
            return
        else:
            build_req(city=CITIES[int(choice) - 1].lower())
    except ValueError:
        print '~Bad Selection!\n'
        return

def front_story():
    build_req(front_page=True)

def query_sport():
    print '\nSelect a sport:'
    for sport in enumerate(SPORTS, 1):
        print '    [%d] %s' % (sport[0], sport[1])
    choice = raw_input('> ')
    try:
        if not any(i==int(choice) for i in range(1, 5)):
            print '~Bad Selection\n'
            return
        else:
            sports = SPORTS.keys()
            sport_choice = sports[int(choice) - 1].lower()
            return sport_choice
    except ValueError:
        print '~Bad Selection\n'
        return

def team(sport):
    print '\nEnter a team name:'
    team = raw_input('> ')
    build_req(sport=sport, team=team)

def athlete(sport):
    print '\nEnter an athlete name:'
    athlete = raw_input('> ')
    build_req(sport=sport, athlete=athlete)

def sportline(sport_choice):
    build_req(sport=sport_choice)

def team_ids(sport, league, team):
    req = 'http://api.espn.com/v1/sports/%s/%s/teams?apikey=' % (sport.lower(), league) 
    response = requests.get(req + apikey)
    json_data = response.json()
    teams = collections.defaultdict(list)
    all_ids = parse_teams(json_data, teams)
    if team.lower() in all_ids.keys():
        return all_ids[team.lower()][1]
    return

def athlete_ids(sport, league, athlete):
    offset = 0
    diff = None
    while True:
        req = 'http://api.espn.com/v1/sports/%s/%s/athletes?offset=%d&apikey=' % (sport.lower(), league, offset)
        response = requests.get(req + apikey)
        json_data = response.json()
        athletes = collections.defaultdict(list)
        all_ids = parse_athletes(json_data, athletes)
        if not all_ids:
            return
        elif athlete.lower() in all_ids.keys():
            return all_ids[athlete.lower()][0]
        time.sleep(0.5)
        if not diff or diff > 5:
            offset, diff = offset_jump(all_ids.keys(), athlete, offset)        
            if diff < 0:
                return
        else:
            offset += 1
    return

def offset_jump(athletes, query, offset):
    last_person = athletes.sort()[-1]
    name = last_person.split()[-1]
    cur_val = ord(name[0])
    query = last_person.split()[-1]
    query_val = ord(query[0])
    if query_val - cur_val >= 0:
        diff = 0
    elif query_val - cur_val <= 10:
        diff = query_val - cur_val
        offset += 100
    return offset, query        

def build_req(sport=None, team=None, athlete=None, city=None, front_page=False):
    if athlete:
        sport = sport.capitalize()
        league = SPORTS[sport]
        athlete_id = athlete_ids(sport, league, athlete)
        if athlete_id:
            sport = sport.lower()
            req = 'http://api.espn.com/v1/sports/%s/%s/athletes/%d/news?apikey=' % (sport, league, athlete_id)
        else:
            print "Found no athlete %s" % athlete
            return
    elif team:
        sport = sport.capitalize()
        league = SPORTS[sport]
        team_id = team_ids(sport, league, team)
        if team_id:
            sport = sport.lower()
            req = 'http://api.espn.com/v1/sports/%s/%s/teams/%s/news?apikey=' % (sport, league, team_id)
        else:
            print "Found no team %s" % team
            return
    elif front_page:
        req = 'http://api.espn.com/v1/sports/news/headlines/top?apikey='
    elif city:
        req = 'http://api.espn.com/v1/cities/%s/news/headlines?apikey=' % city
    else:
        sport = sport.lower()
        league = SPORTS[sport.capitalize()]
        req = 'http://api.espn.com/v1/sports/%s/%s/news/headlines?apikey=' % (sport, league)
    response = requests.get(req + apikey)
    json_data = response.json()
    headlines = parse_headlines(json_data, [])
    news_handle(headlines)

def news_handle(headlines):
    print "-Headlines-"
    for hdline in enumerate(headlines, 1):
        print '  [%d] %s' % (hdline[0], hdline[1])
    return

