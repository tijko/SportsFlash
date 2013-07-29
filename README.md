#SportsFlash


SportsFlash to get the latest updates from [ESPN.com](http://www.espn.com).  
You can specify a team, athlete, area or the front page sports headlines in 
general.

Right now the headlines can be read only, some kind of selection of a headline to
open a page in your browser might be added in too.

All the headline titles return to your terminal. and you need an apikey from [API](developers.espn.com/docs).

This could be easily wrapped to interface with an extension to display in a browser as a
news scroll or be used as a feed to use with forms or display on a larger page.


##usage

    python SportsFlash/main.py -h
    usage: main.py [-h] [-H | -s | -t | -a | -m]

    SportsFlash gives you the latest headlines from ESPN. With options for a
    specific league, team, player or major sports area. Links returned can
    optionally be followed up further to the article.

    optional arguments:
      -h, --help        show this help message and exit
      -H, --headlines   Show all headlines on ESPN front page.
      -s, --sport       Show all headlines for specific sport.
      -t, --team        Show all headlines for specific team.
      -a, --athlete     Show all headlines for specific athlete.
      -m, --major_city  Show all headlines for major area.

The python requests module is used in SportsFlash and will need to be installed to use.
