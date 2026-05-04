from datetime import datetime
from zoneinfo import ZoneInfo
import time
import os





def tod():
	time_of_day = datetime.hour()
	if 6 < time_of_day < 17:
		print("Day")
	
	elif 18 < time_of_day < 20:
		print("Evening")
	
	elif 5 > time_of_day > 21:
		print("Night")
	
	else:
		print(time_of_day)


def show_time(city, timezone):
	current_time = datetime.now(ZoneInfo(timezone))
	print(city + ": " + current_time.strftime("%A, %B %d %I:%M %p %Z"))



def show_local():
	local_time = datetime.now()
	print("Local: " + local_time.strftime("%I:%M %p") + "at ", tod())



cities = [
	{"name": "New York", "timezone": "America/New_York"},
	{"name": "London", "timezone": "Europe/London"},
	{"name": "Tokyo", "timezone": "Asia/Tokyo"},
	{"name": "Los Angeles", "timezone": "America/Los_Angeles"},
	{"name": "Paris", "timezone": "Europe/Paris"},
	{"name": "Sydney", "timezone": "Australia/Sydney"},
	{"name": "Dubai", "timezone": "Asia/Dubai"},
	{"name": "Singapore", "timezone": "Asia/Singapore"},
	{"name": "Hong Kong", "timezone": "Asia/Hong_Kong"},
	{"name": "Kolkata", "timezone": "Asia/Kolkata"},
	{"name": "Sāo Paulo", "timezone": "America/Sao_Paulo"},
	{"name": "Moscow", "timezone": "Europe/Moscow"},
]




try:
	while True:
		os.system("clear")
		show_local()
		for city in cities:
			show_time(city["name"], city["timezone"])
		
		print("Last Updated: ", datetime.now().strftime("%I:%M %p")) 
		interval = 60 - datetime.now().second 
		time.sleep(interval)
except KeyboardInterrupt:
	pass
