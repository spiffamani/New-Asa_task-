<<<<<<< HEAD
	investment_value = 0
return_peryear = 0
Roi_percentage = 0
Roi_return = 0
roi_inpercentage = 0
Roi = 0



principal = int(input('Enter principal: '))

interestrate = int(input('Enter rate:')) / 100

numberofyears = int(input('Enter number of years:'))



investment_value = principal * (1 + interestrate) ** numberofyears

return_peryear =  investment_value  - principal
print( 'Return per year is ' , return_peryear)

Roi_return = (investment_value - principal ) / principal

roi_inpercentage =( principal * Roi_return ) / 100

Roi = principal + return_peryear

print( 'ROI return is ' , Roi )
print(f" {Roi:.2f}")


=======
	investment_value = 0
return_peryear = 0
Roi_percentage = 0
Roi_return = 0
roi_inpercentage = 0
Roi = 0



principal = int(input('Enter principal: '))

interestrate = int(input('Enter rate:')) / 100

numberofyears = int(input('Enter number of years:'))



investment_value = principal * (1 + interestrate) ** numberofyears

return_peryear =  investment_value  - principal
print( 'Return per year is ' , return_peryear)

Roi_return = (investment_value - principal ) / principal

roi_inpercentage =( principal * Roi_return ) / 100

Roi = principal + return_peryear

print( 'ROI return is ' , Roi )
print(f" {Roi:.2f}")


>>>>>>> b37443c0a807d4a76c8e3d97c7fe6054de7312e3
