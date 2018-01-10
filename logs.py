#!/usr/bin/python

import re, sys, datetime

months = dict(Jan='01',
			Feb='02',
			Mar='03',
			Apr='04',
			May='05',
			Iun='06',
			Jul='07',
			Aug='08',
			Sep='09',
			Oct='10',
			Nov='11',
			Dec='12')

def main ():
	for arg in sys.argv[1:]:
		print (arg)

fh = open ("test1.log", "r");
rate = {}
total = {}
curr_datetime = " "

for line in fh:
	#extragere elemente din linia citita
	date = re.findall('\[([^\]]*)\]', line)
	split = date[0].split("/")
	day = split[0]
	month = months[split[1]]
	split = split[2].split(":")
	year = split[0]
	hour = split[1]
	minute = split[2]
	date = line.split(" ")
	error = date[8]
	date = re.findall(' \/.+.html', line)
	blackspace = date[0].split(" ")
	endpoint = blackspace[1]
	interval = 1

	datetime = year + '-' + month + '-' + day + 'T' + hour + ':' + minute

	#vector de frecventa in care numar rata de succes
	if curr_datetime != datetime:
		for elem in total:
			if elem in rate:
				total[elem] = rate[elem] * 100 / total[elem]
			else:
				total[elem] = 0.0
		x = sorted(total)
		for elem in x:
			print (curr_datetime, interval, elem, "%.2f" % total[elem])
		curr_datetime = datetime
		rate = {}
		total = {}

	if error[0] == '2':
		if not endpoint in rate:
			rate[endpoint] = 1
		else:
			y = rate[endpoint]
			rate[endpoint] = y + 1

	if not endpoint in total:
		total[endpoint] = 1
	else:
		z = total[endpoint]
		total[endpoint] = z + 1

for elem in total:
	if elem in rate:
		total[elem] = rate[elem] * 100 / total[elem]
	else:
		total[elem] = 0.0
x = sorted(total)
for elem in x:
	print (curr_datetime, interval, elem, "%.2f" % total[elem])

fh.close()

if __name__ == "__main__":
    main()
