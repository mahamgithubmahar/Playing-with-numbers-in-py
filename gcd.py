smallernumber=int(input("Enter a smaller number: "))
biggernumber=int(input("Enter a bigger number: "))

while smallernumber>0:
    numberstore=smallernumber
    smallernumber=biggernumber%smallernumber
    biggernumber=numberstore

print("The hcf/gcd is", biggernumber)