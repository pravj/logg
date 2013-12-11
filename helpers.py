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

# do something with quartile values and commits
def rank(a,b,c,n):
	if(n==blank):
		return blank
	elif(n in days):
		return n
	elif(n==0):
		return 0
	elif((n>0) and (n<=a)):
		return 1
	elif((n>a) and (n<=b)):
		return 2
	elif((n>b) and (n<=c)):
		return 3
	else:
		return 4

# show appropriate box in calendar
def render(n):
	# xterm color values for small calendar-box's background
	colors = [254,71,47,2,22]
	square = '■'
	if(n==blank):
		return blank
	# supposed to be anyone of [0,1,2,3,4] (ranked)
	elif(n<5):
		return '\033[38;5;%dm%s\033[0m'%(colors[int(n)],square)
	# supposed to be elements in lists 'days' and 'months' and color-palatte text
	else:
		return '\033[38;5;46m%s\033[0m'%(n)
