
sen = input("enter a sentence to reverse: ")
print(*(reversed(sen)))
print("".join(reversed(sen)))
print(sen[::-1])
for i in range(len(sen)-1, -1, -1):
    print(sen[i], end="")


