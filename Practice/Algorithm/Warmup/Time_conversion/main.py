#Write up to Hackerrank Time Conversion
#Challenge : https://www.hackerrank.com/challenges/time-conversion

import time
print(time.strftime('%H:%M:%S', time.strptime(str(input()), '%I:%M:%S%p')))