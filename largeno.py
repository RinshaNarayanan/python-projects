
n = [1, 2, 3]

def largest_no(n):
    largest_no = n[0]

    for i in range(len(n)):
        if n[i] > largest_no:
            largest_no = n[i]
    return largest_no

result = largest_no(n)
print result


