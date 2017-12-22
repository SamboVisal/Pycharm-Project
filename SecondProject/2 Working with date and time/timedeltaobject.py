from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import pytz
#construct timedelta and print it
for tz in pytz.all_timezones:
	print(tz);
