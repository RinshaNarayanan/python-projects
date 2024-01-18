n = input ("Enter Number")
def sum_of_no(n):
    sum = 0 

    for i in range(1,n+1):
         sum += i

    return sum

         


result = sum_of_no(n)
print(result)