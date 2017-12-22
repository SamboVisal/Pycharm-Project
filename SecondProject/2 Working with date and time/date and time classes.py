
from datetime import date;
from datetime import time;
from datetime import datetime;

def main():
 today = date.today();
 print ("Today date is ", today);
 #date month and year as individual
 print ("Date component: ",today.day, today.month, today.year)
 #retrieve today's weekday (0=Monday, Sunday=6)
 print("Today's weekday #: ", today.weekday());
 #datetime OBJECT
 #it will display both date and time
 day = datetime.today();
 print("The current date and time is ",  day)
 day = datetime.time(datetime.now())
 print("The current time is ",day)
 wb = date.weekday(today)
 days=["Monday","Tuesday","Webnesday","Thursday","Friday","Saturday","Sunday"];
 print("Week day is",wb);
 print("day of week day is",days[wb]);
if __name__ == '__main__':
	main();