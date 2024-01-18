string = input("Enter the string")
count = 0
consonants_count = 0
for i in range(len(string)-1,-1,-1):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    if string[i] in vowels:
        count = count+1
    else:
        consonants_count = consonants_count+1
print(count)  
print(consonants_count)      