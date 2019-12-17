

#random numbers insert into database

import random
import sqlite3
import time

for x in range(10):
    number = random.randrange(1,10)
    print (number)
    unix=time.time()
    print(unix)
