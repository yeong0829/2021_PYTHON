import math
print(math.ceil(3.5))  #4   올림
print(math.ceil(3.4))  #4
print(math.floor(3.5)) #3   내림
print(math.floor(3.4)) #3
print(round(3.5))#4  반올림
print(round(3.4)) #3
print(math.pow(2, 10)) #1024.0
print(math.sin(math.pi/2)) #1.0


import random
print('-'*20)
print(random.random())          #
print(random.randrange(1, 10))
print(random.randint(1, 10))

list1=['김치찌개', '비빔면', '잠']
print(random.choice(list1))

print('befor: ', list1)
random.shuffle(list1)
print('after: ', list1)

print(random.sample(list1, 2))

import datetime
print('-'*20)
now = datetime.datetime.now()
birthday = datetime.datetime(2004, 8, 29)
print(birthday)
print(now-birthday)
