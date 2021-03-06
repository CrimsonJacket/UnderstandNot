import json
import sys

data = {}
building_block = []
sentence = ''
time_sector = 1
current_time = 0.0
TIMING = 1
timing_block = []
captions = []
with open('out','r') as f:
	data = json.load(f)

for block in data['response']['results']:
	for tiny_block in block['alternatives']:
		for word in tiny_block['words']:
			building_block.append(word['word'])
			if 'endTime' in word:
				end_time = word['endTime']
				end_time = end_time[:-1]
				end_time = float(end_time)
			if end_time > time_sector * TIMING:
				sentence = ' '.join(building_block)
				building_block = []
				output = (current_time, end_time, sentence)
				captions.append(output)
				current_time = end_time
				time_sector = end_time/1 + 1

sentence = ' '.join(building_block)
output = (current_time, end_time, sentence)
captions.append(output)

def formatTiming(x): 
	time_str = str(x)
	time_str = time_str[:-1]
	time_str = time_str.split('.')
	minute,sec = divmod(int(time_str[0]),60)
	hour, minute = divmod(minute, 60)
	time_str[0] = sec
	time_str.insert(0, minute)
	time_str.insert(0, hour)
	str_format = '{:02}:{:02}:{:02},{:0<3}'.format(time_str[0], time_str[1], time_str[2], time_str[3])
	return str_format

for x,y in enumerate(captions):
	print(x+1)
	str_format = '{} --> {}'.format(formatTiming(y[0]), formatTiming(y[1]))
	print (str_format)
	print (y[2])
	print('')