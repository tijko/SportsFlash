#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
from lib.retrieve_flash import * 


def options():
    parser = argparse.ArgumentParser(description='''SportsFlash gives you the latest headlines from ESPN.

                                                    With options for a specific league, team, player or
                                                    major sports area.
                                                    
                                                    Links returned can optionally be followed up further 
                                                    to the article.
                                                 ''')
    mutex_arg = parser.add_mutually_exclusive_group()
    mutex_arg.add_argument('-H', '--headlines', help='Show all headlines on ESPN front page.', action='store_true')
    mutex_arg.add_argument('-s', '--sport', help='Show all headlines for specific sport.', action='store_true')
    mutex_arg.add_argument('-t', '--team', help='Show all headlines for specific team.', action='store_true')
    mutex_arg.add_argument('-a', '--athlete', help='Show all headlines for specific athlete.', action='store_true')
    mutex_arg.add_argument('-m', '--major_city', help='Show all headlines for major area.', action='store_true')
    parse = parser.parse_args()
    return parse

def main(opt):
    if len(sys.argv) < 2:
        print 'Run with a "-h" parameter for help'
        return        
    elif opt.major_city:
        city()
    elif not opt.headlines:
        sport_choice = query_sport()
        if not sport_choice:
            return
        elif opt.team:
            team(sport_choice)
        elif opt.athlete:
            athlete(sport_choice)
        else:
            sportline(sport_choice)
    else:
        front_story()

if __name__ == '__main__':
    opt = options()
    main(opt)

