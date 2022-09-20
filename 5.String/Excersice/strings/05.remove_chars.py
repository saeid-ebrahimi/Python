

sen = input("enter a sentence to remove chars: ")
chars = input("enter the characters to remove from text: ")

sen1 = sen
for ch in chars:
    sen1 = sen1.strip(ch)   # to remove laeding and ending chars
    print(sen1)
sen2 = sen
for ch in chars:
    sen2 = sen2.replace(ch, '')
print(sen1)
print(sen2)




# hello my dear frined, I'm gonna leave this cruel world for ever.









