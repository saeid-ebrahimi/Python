
def cesar_encrypt(raw_text, step):
    upper_cases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_cases = "abcdefghijklmnopqrstuvwxyz"
    out_text = ''
    for let in raw_text:
        if let in upper_cases:
            index = upper_cases.index(let)
            new_index = (index + step) % 26
            out_text += upper_cases[new_index]
        elif let in lower_cases:
            index = lower_cases.index(let)
            new_index = (index + step) % 26
            out_text += lower_cases[new_index]
    return out_text


text = input("enter a text to encrypt: ")
key = int(input("enter cesar encrypting key number: "))
print(cesar_encrypt(text, key))








