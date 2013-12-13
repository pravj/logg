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
from viewbar import cal_hour,cal_week,cal_month
from gitview import git_log_calendar

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
				exc = ("type main.py --timespan=<hour/week/month> [for corresponding timespan]\n"
					   "Example : for mothly git history use main.py --timespan=month")
				# warn : wrong user input
				print exc
		else:
			print __doc__

	elif args['calc']:
		if args['--past'] is None:
			git_log_calendar(past=None)
		elif(re.match(r'^\d+$',args['--past'])):
			git_log_calendar(args['--past'])
		else:
			# warn : wrong user input
			print "option --past should be a number"

	else:
		print __doc__

if __name__ == '__main__':
	main()
