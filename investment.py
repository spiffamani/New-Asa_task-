# Investment Return
total = 0
principal = int(input('Enter principal amount'))
annualrate = int(input('Enter annual rate'))
numberofyears = int(input('Enter number of years'))

annualrate = (annualrate + 1) ** numberofyears
total = principal * annualrate
print( 'The investment return is ' , total)
