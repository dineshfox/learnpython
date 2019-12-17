import math

#a=2
#b=20
loc = 40
pm=6

#pm=math.sqrt(a)+b*math.sqrt(loc)

b = (pm - math.sqrt(a))/math.sqrt(loc)

print (b)

#calculate a and b constant 
for a in range(10):
    b = (pm - math.sqrt(a))/math.sqrt(loc)
    print(a,b)
    
