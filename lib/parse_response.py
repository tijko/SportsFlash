#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parse_athletes(json, athletes):
    if isinstance(json, list):
        for i in json:
            athletes = parse_athletes(i, athletes)
    elif isinstance(json, dict):
        for k in json.keys():
            if k == 'displayName' and json[k] not in athletes:
                athlete = json[k].lower()
                athletes[athlete].append(json['id'])
            else:
                athletes = parse_athletes(json[k], athletes)
    return athletes

def parse_headlines(json, hdlines):
    if isinstance(json, list):
        for i in json:
            hdlines = parse_headlines(i, hdlines)
    elif isinstance(json, dict):
        for k in json.keys():
            if k == 'linkText' and json[k] not in hdlines:
                hdlines.append(json[k])
            else:
                hdlines = parse_headlines(json[k], hdlines)
    return hdlines

def parse_teams(json, teams):
    if isinstance(json, list):
        for i in json:
            teams = parse_teams(i, teams)
    elif isinstance(json, dict):
        for k in json.keys():
            if k == 'name' and json[k] not in teams and 'location' in json.keys():
                club_name = json['name'].lower()
                teams[club_name].extend([json['location'], json['id']])
            else:
                teams = parse_teams(json[k], teams)
    return teams
