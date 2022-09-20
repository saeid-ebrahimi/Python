

sen = input("enter a sentence : ")
new_sen = ''
for ch in sen:
    if ch.islower():
        new_sen += ch.upper()
    elif ch.isupper():
        new_sen += ch.lower()
    else:
        new_sen += ch
print(new_sen)
# Hello my dear friend, I'm gonna leave this cruel world for ever.









