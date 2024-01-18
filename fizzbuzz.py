n = input("Enter the number:")
string = ""
for i in range(1,n+1):
    if i%3==0 and i%5==0 :
        string = "fizzbuzz"
    elif i%3 == 0 :
       string = "fizz"
    elif i%5==0 :
        string ="buzz"
    
    else :
        string =""
    message = "{0}  {1}".format(i,string)

    print(message)