# password input

passrange1 = 8
passrange2 =16


number = input ('Enter password: ')
if passrange1 < len(number):
    print('very weak')

if len(number) == passrange1:
    print( 'weak ')

if passrange1  <= len(number) <=  (passrange2):

   print('strong')

if len(number)  >= passrange1  :
    print('very strong')