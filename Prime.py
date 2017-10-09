#!/usr/bin/python
num1=int(input('Enter value to find if it is Prime:'))
count=0
if (num1<=0):
  print ("Enter Positive number other than 0 and 1")
elif (num1==1):
  print ("1 is neither Prime nor composite number.")
else:
    for i in range (2,num1):
      if num1%i==0:
        count+=1
    if (count==0):
      print (num1, 'is a Prime number')
    else:
      print (num1,'not a Prime number')
