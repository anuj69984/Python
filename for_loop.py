import random
import sys
import os

my_list=['phone','tab','charger','speaker']
for x in my_list:
	print(x)

for y in range(0,10):
	print(y," ",end="")	

print('\n')

for x in [1,2,3,4,5,6,]:
	print(x," ",end="")	
print('\n')	

random_number=random.randrange(0,10)
while(random_number !=4):
	print(random_number," ",end="")
	random_number=random.randrange(0,10)
print('\n')
i=0
while(i<=10):
	if(i%2==0):
		print("Even number : ",i)
	else:
		print("odd number : ",i)	
	i=i+1	