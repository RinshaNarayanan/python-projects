word = input("enter the word:")
reverse = ""
for i in range(len(word)-1,-1, -1):
    reverse = reverse + word[i]


if reverse == word:
    print("palindrome")
else:
    print("not")
