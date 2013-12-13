# -*- encoding:utf-8 -*-

# to left blank somewhere in calendar
blank = " "

# block used for bar-graph and boxes in calendar
square = '■'

# weekdays with 'Sunday' as first day
days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

# think on maping things
hours = ['00','01','02','03','04','05','06','07','08','09','10','11']
for i in range(len(hours)):
	hours.append(str(int(hours[i])+12))
