# -*- encoding:utf-8 -*-

import calendar
from subprocess import Popen, PIPE
from constants import blank,days

# return a word(string) with or without basic pluralization ??
def grammer(freq):
	if(freq>1):
		return 'commits'
	else:
		return 'commit'

# returns result of a shell command
def command(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    p.wait()
    return p.stdout.read()[:-1]

# weekday [because, python returns 0 for 'Mon' and 6 for 'Sun']
def weekday(a,b,c):
	n = calendar.weekday(a,b,c)
	if(n==6):
		return 0
	else:
		return n+1
