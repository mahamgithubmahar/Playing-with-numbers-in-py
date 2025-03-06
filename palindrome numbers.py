number=int(input("Enter a number: "))
temp=number
reversed_number=0

while temp>0:
    digit=temp%10
    reversed_number=reversed_number*10+digit
    temp//=10 #temp=temp//10

if reversed_number==number:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")