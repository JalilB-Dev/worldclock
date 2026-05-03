from datetime import datetime
from zoneinfo import ZoneInfo
import time
import os



def show_time(city, timezone):
	current_time = datetime.now(ZoneInfo(timezone))
	print(city + ": " + time.strftime("%A, %B %d %I:%M %p %Z"))



def local(city, timezone):
	local_time = localtime(ZoneInfo(timezone))
	print(time.strftime("%I:%M %p %Z"))



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

while True:
	os.system("clear")
	for city in cities:
		show_time(city["name"], city["timezone"])
	print("Last Updated: ", local) 
	time.sleep(60)
	
