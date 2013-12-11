import os
import re
import time
import calendar
from datetime import timedelta,date
from helpers import command,rank,render,weekday
from constants import blank,days,months

def git_log_calendar(past=None):
	# help in finding starting date
	os.system('git log --reverse --format="%ci" > first.txt')
	with open('first.txt','r') as f:
		data = f.read()
	f.close()
	first = re.match(r'(\d+)\-(\d+)\-(\d+)',data).groups()
	os.system('rm first.txt')

	today = date.today()
	# lastyear, just 365 days in past
	ly = today - timedelta(days=365)

	# project starting date
	startdate = date(int(first[0]),int(first[1]),int(first[2]))

	if past is not None:
		past = int(past)
		# same as showing generally
		if(past == 1):
			pass
		else:
			# if history is available that back
			if((today-startdate).days > (past-1)*365):
				today = today - timedelta(days=365*(past-1))
				ly = today - timedelta(days=365)
			else:
				# show perfection here
				print 'This project does\'t have that long commit history'
				print 'Showing current year contribution instead'

	# today's date variables
	tyear = today.year
	tmonth = today.month
	tday = today.day

	# represent each day of calendar, intially starting day of calendar
	cursor = ly + timedelta(days=1)
		
	# total day count
	count = 0

	# using it like 2D matrix for 53 week-data [52 week + 1 day]
	weekly = {}

	# weekday on ending date of calendar, used to leave 6 blank spaces
	wd = weekday(today.year,today.month,today.day)

	# labels on leftside of calendar for weekdays
	weekly[0] = days

	# month's label
	monthLabel = "    "
	mon = cursor.month
	monthLabel = render(monthLabel + months[mon-1])
	gap1 = 2

	# to keep first month in some extra left
	flag=True

	# organising last 365 day's commit logs in 53 lists[of 7 length]
	while(cursor <= today):
		# mantaining spaces in month label, not so good
		if(cursor.month != mon):
			gap2 = len(weekly)

			# it temporary fixes alignment, if a month starts on sunday, will check
			if(weekday(cursor.year,cursor.month,cursor.day)==0):
				gap2 = gap2+1

			# to keep first month in some extra left
			if(flag):
				monthLabel = monthLabel + " "
				flag = False

			mon = cursor.month				
			monthLabel = monthLabel + render(" "*(2*(gap2-gap1)-3) + months[cursor.month-1]) 
			gap1 = gap2
		
		# marking as ' '(blank) for days of first week that are not counted in a year
		if(count==0):
			weekly[1] = []
			for j in range(0,wd):
				weekly[1].append(blank)

		if(cursor.month < 10):
			nm = '0%s'%(str(cursor.month))
		else:
			nm = cursor.month

		if(cursor.day < 10):
			nd = '0%s'%(str(cursor.day))
		else:
			nd = cursor.day
		
		cmt = int(command('git log --format=format:"%ci" ' + ' | grep "%d-%s-%s" | wc -l'%(cursor.year,nm,nd)))
		
		# filling in first week if 7 days are not complete 
		if(len(weekly[1])<=6):
			weekly[1].append(cmt)

		# mantaining calendar with first and last week
		if(count >= (7-wd)):
			# new list for new week
			if((count+wd)%7 == 0):
				weekly[((count+wd)/7)+1] = []
			weekly[((count+wd)/7)+1].append(cmt)
		
		count = count + 1
		cursor = cursor + timedelta(days=1)


	# suffer-sorting :D
	fake = []
	for i in range(1,len(weekly)):
		for j in range(len(weekly[i])):
			p = weekly[i][j]
			if(p!=0):
				fake.append(p)

	fake = sorted(fake)
	lf = len(fake)

	# quartile values
	Q1 = fake[lf/4]
	Q2 = fake[lf/2]
	Q3 = fake[3*lf/4]
	
	# as it is not defined already
	for i in range(wd+1,7):
		weekly[53].append(blank)

	# month label on top
	print monthLabel

	# generating the calendar
	for k in range(0,7):
		x = ''
		for l in range(0,54):
			x = '%s %s'%(x,(render(rank(Q1,Q2,Q3,weekly[l][k]))))
		print x
	
	# less-more indicator color palatte
	palatte = render('     Less ')
	for x in range(5):
		palatte = palatte + render(x) +  ' '
	palatte = palatte + render(' More')
	print palatte
