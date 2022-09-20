
sen = input("Enter a sentence: ")
for ch in sen[1::2]:
    print(ch, end=" ")
print()
for i in range(1, len(sen), 2):
    print(sen[i], end=" ")
print()
for i in range(len(sen)):
    if i % 2 == 0:
        print(sen[i], end=" ")
print()
print(sen[1::2])
