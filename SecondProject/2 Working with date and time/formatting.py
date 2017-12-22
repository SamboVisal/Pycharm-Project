from datetime import datetime
from datetime import timedelta

def main():
	now = datetime.now()
	#%y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - date of month
	print(now.strftime("%Y")); #full year with century
	print(now.year);
	print(now.strftime("%y")); #only year not with century
	print(now.strftime("%b")) #not full word of month
	print(now.strftime("%B"))
	print(now.strftime("%A"))
	print(now.strftime("%d"))
	print(now.strftime("%d, %b, %Y,%a"))
	print("Local date,time")
	# %c - local's date and time, %x - local's date, %X - local's time
	print(now.strftime("%c"))
	print(now.strftime("%x"))
	print(now.strftime("%X"))
	print("Time formatting")
	# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - local's AM/PM
	print (now.strftime("%I:%M:%S:%p"))
	print(now.strftime("%H:%M"))


	credits()
if __name__ == '__main__':
	main()