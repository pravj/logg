# -*- encoding: utf-8 -*-
"""trying something

Usage:
  main.py what
  main.py view [--timespan=<hour/week/month>] 
  main.py calc [--past=N(years)]

Options:
  (-h | --help)                 "Show this help-message screen"
  --version                 	"Show current version"

"""

import os
import re
from docopt import docopt
from constants import blank,hours,days,months
from gitview import git_log_calendar

# display bar graph
def display(key, value, Max=False):
	if(len(key) == len(value)):
		tick = '▇'
		if(Max):
			maxindex = 0
			for i in range(len(value)):
				if(value[i]>value[maxindex]):
					maxindex = i

			maxvalue = value[maxindex]
			return [maxindex,maxvalue]

		else:
			Sum = 0
			for j in range(len(value)):
				Sum = Sum + value[j]

			for i in range(len(key)):
				perc = (value[i]*100.0/Sum)
				result = tick*int(perc)
				_perc_ = "(" +str(perc)[:4]+ "%)"
				print "%s %s %s"%(key[i],_perc_,result)
	else:
		print 'r u mad'

def cal_hour(Max=False):
	hour_commit = []
	os.system('git log --reverse --format="%cd" > new.txt')

	for j in range(len(hours)):
		x = 0
		with open('new.txt','r') as f:
			data = f.read()

		x = data.count(' %s:'%(hours[j]))
		hour_commit.append(x)
	f.close()
	os.system('rm new.txt')

	if(Max):
		return display(hours,hour_commit,True)
	else:
		display(hours,hour_commit,False)

def cal_week(Max=False):
	days_commit = []
	os.system('git log --reverse --format="%cd" > new.txt')

	for i in range(len(days)):
		x = 0
		with open('new.txt', 'r') as f:
			data = f.read()

		x = data.count('%s'%(days[i]))
		days_commit.append(x)
	f.close()
	os.system('rm new.txt')

	if(Max):
		return display(days,days_commit,True)
	else:
		display(days,days_commit,False)

def cal_month(Max=False):
	mon_commit = []
	os.system('git log --reverse --format="%cd" > new.txt')

	for i in range(len(months)):
		x = 0
                with open('new.txt', 'r') as f:
                	data = f.read()
                
                x = data.count('%s'%(months[i]))
                mon_commit.append(x)
       	f.close()
	os.system('rm new.txt')

	if(Max):
		return display(months,mon_commit,True)
	else:
		display(months,mon_commit,False)

def main():
	args = docopt(__doc__, version='0.1')
	
	if args['what']:
		print "git logs"

	elif args['view']:
		if args['--timespan'] is not None:
			if(args['--timespan']=='hour'):
				cal_hour()
			elif(args['--timespan']=='week'):
				cal_week()
			elif(args['--timespan']=='month'):
				cal_month()
			else:
				# show perfection here
				print "type try.py --timespan=<hour/week/month> [for corresponding timespan]"
				print "Example : for mothly git history use try.py --timespan=month"
		else:
			print __doc__

	elif args['calc']:
		if args['--past'] is None:
			git_log_calendar(past=None)
		elif(re.match(r'^\d+$',args['--past'])):
			git_log_calendar(args['--past'])
		else:
			print 'option --past should be a number' #show perfection here

	else:
		print __doc__

if __name__ == '__main__':
	main()
