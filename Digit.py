# Seperating  Digit 


number = int(input('Enter five digit number'))

firstnumber = 0:
secondnumber= 0:
thirdnumber = 0:
fourthnumber = 0:
fifthnumber = 0:

firstnumber = number / 10000:
number = number % 10000:
secondnumber = number / 1000:
number = number % 1000:
thirdnumber = number / 100:
number = number % 100:
fourthnumber = number / 10:
number = number % 10:
fifthnumber = number:


print(f" {firstnumber}  + {secondnumber} + {thirdnumber} +  {fourthnumber}  +  {fifthnumber}")
