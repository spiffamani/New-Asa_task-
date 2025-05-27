public  class palindrome{
public static void main(String[] args){

firstnumber = 0;
secondnumber = 0;
thirdnumber = 0;
fourthnumber = 0;
fifthnumber = 0 ;

System.out.print("Enter number");
int userinput = input.nextInt();

firstnumber = userinput / 10000 ;
userinput = userinput - firstnumber * 10000;
secondnumber = userinput / 1000 ;
userinput = userinput - secondnumber * 1000;
thirdnumber = userinput /  100 ;
userinput = userinput / 100;
fourthnumber  =  userinput / 10 ;
userinput = userinput - fourthnumber * 10 ;
fifthnumber = userinput;

if(firstnumber == fifthnumber)
	fifthnumber = firstnumber;

if(secondnumber == fourthnumber)
	fifthnumber = firstnumber;

if(thirdnumber == thirdnumber)
	thirdnumber = thirdnumber;
print( 'palindrome number')

elif:
print(' not palindrome')




