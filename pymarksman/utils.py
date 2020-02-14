from shutil import which
import sys


def die(msg=''):
    '''output msg & quit'''
    if msg:
        print(msg)
    sys.exit()


def get_browser_location():
    '''get chromium location'''
    for loc in (which('chromium'), which('chromium-browser')):
        if loc is not None:
            return loc
