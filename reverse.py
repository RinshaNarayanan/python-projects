n = input("enter the number:")

reverse_no = 0

while n > 0:
    reverse_no = reverse_no * 10 + (n % 10)
    n = n / 10

print(reverse_no)
