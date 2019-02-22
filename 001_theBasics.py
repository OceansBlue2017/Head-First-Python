# First Line of Code to test
'''
colors = ['Blue', 'Red', 'Brown', 'Hazel']
i = 0
while i < len(colors):
    print("When I was %d, my favorite color was %s" % (i, colors[i]))
    i = i+1
'''

# **************    Head First Python Book  Page 4  Code    **************
'''
from datetime import datetime

odds = [1,  3,  5,  7,  9,  11, 13, 15, 17, 19,
       21, 23, 25, 27, 29,  31, 33, 35, 37, 39,
       41, 43, 45, 47, 49,  51, 53, 55, 57, 59]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print('This minute seems a little odd.')
else:
    print('Not an odd minute.')
'''
# **************    Head First Python Book  Page  4  Code    **************

# **************    Head First Python Book  Page 11  Code    **************
'''
import datetime
Date = datetime.date.isoformat(datetime.date.today())
print(Date)

import time
T = time.strftime('%H:%M')
print(T)

import html
htMl00 = html.escape('This HTML fragment contains a <script>script</script> tag.')
print(htMl00)
htMl01 = html.escape("I &hearts; Python's &lt;standard library&gt;")
print(htMl01)
'''
# **************    Head First Python Book  Page 11  Code    **************

# **************    Head First Python Book  Page 17  Code    **************
'''
from datetime import datetime
today = datetime.today()
if today == 'Saturday':
    print('Party! ****')
elif today == 'Sunday':
    print('Recovery Day')
else:
    print('Work, Work, and more Work')
'''

# **************    Head First Python Book  Page 17  Code    **************

# **************    Head First Python Book  Page 39 Nook  Code    **************
'''
for s in [1, 2, 3,]:
    print(s)

for num in range(3):   #
    print("it's alomst 3:00 AM")

num = 0
while num < 5:   #
    print("it's alomst 15:00 AM Ha ha ha")
    num = num +1
    
    '''
# **************    Head First Python Book  Page 39 Nook  Code    **************

# **************    Head First Python Book  Page 45 Nook Code    **************

from datetime import datetime
import random
import time


odds = [1,  3,  5,  7,  9,  11, 13, 15, 17, 19,
       21, 23, 25, 27, 29,  31, 33, 35, 37, 39,
       41, 43, 45, 47, 49,  51, 53, 55, 57, 59]

for n in range(3):   #
    right_this_minute = datetime.today().minute
    waitTime = random.randint(1, 5)
    time.sleep(waitTime)
    if right_this_minute in odds:
        print('This minute seems a little odd.  ' + 'and wait time was '+str(waitTime))
    else:
        print('Not an odd minute.  ' + 'And wait time was '+str(waitTime))




"""
num = 0
while num < 5:   #
    print("it's alomst 15:00 AM Ha ha ha")
    num = num +1
"""

# **************    Head First Python Book  Page 45 Nook Code    **************


