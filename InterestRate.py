<<<<<<< HEAD
  




principal = int(input(' Enter principal amount'))
 
annualrate = int(input('Enter annual interest rate'))

years = int(input('Enter yearly duration rate'))

rate = annualrate / 100 /12 

month = years * 12

sumrate = rate + 1
sumrate1 = sumrate ** month
sumrate2 = sumrate1 * rate
sumrate3 = sumrate1 - 1;

monthlyrate = (principal * sumrate2)   / sumrate3

number_fraction = round(monthlyrate , 2)

print('monthly rate is '  '$',number_fraction)
 





















=======
  




principal = int(input(' Enter principal amount'))
 
annualrate = int(input('Enter annual interest rate'))

years = int(input('Enter yearly duration rate'))

rate = annualrate / 100 /12 

month = years * 12

sumrate = rate + 1
sumrate1 = sumrate ** month
sumrate2 = sumrate1 * rate
sumrate3 = sumrate1 - 1;

monthlyrate = (principal * sumrate2)   / sumrate3

number_fraction = round(monthlyrate , 2)

print('monthly rate is '  '$',number_fraction)
 





















>>>>>>> b37443c0a807d4a76c8e3d97c7fe6054de7312e3
