n= input("enter the number")
isPrime = True
for i in range(2,n):
    remainder =  n%i
    if remainder==0:
        isPrime = False
        break

if isPrime:
    print("prime")
else:
    print("not prime")
    
