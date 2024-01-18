n = input("enter the number=")
k = input("enter the 2nd number:")
for i in range(1,k+1):
    a = i * n
    string = "{0}*{1}={2}".format(i,n,a)
    print(string)

    