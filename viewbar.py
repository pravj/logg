# -*- encoding:utf-8 -*-

import os
from constants import hours,days,months,square
from helpers import render,grammer

# display bar graph
def display(key,value,Max=False):
	if(len(key) == len(value)):
		if(Max):
			maxindex = 0
			match = max(value)
			maxs = []
			for i in range(len(value)):
				if(value[i]>=match):
					maxindex = i
					maxs.append(maxindex)

			# returns list of maximum's indexes
			return maxs

		else:
			Sum = 0
			for j in range(len(value)):
				Sum = Sum + value[j]
			
			maxs = display(key,value,True)

			for i in range(len(key)):
				perc = (value[i]*100.0/Sum)
				result = square*int(perc)
				_perc_ = "(" +str(perc)[:4]+ "%)"
				# highlights maximum's
				if i in maxs:
					to_show = "%s %s %s"%(render(key[i]),render(_perc_),render(result))
				else:
					to_show = "%s %s %s"%(key[i],_perc_,result)
				if(value[i]!=0):
					to_show = "%s [%d %s]"%(to_show,value[i],grammer(value[i]))
					print to_show
				else:
					print to_show


	else:
		print "you messed up.."

# calculate the hourly bar-graph
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

# calculate the weekly bar-graph
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

# calculate the monthly bar-graph
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
