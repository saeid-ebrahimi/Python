
def character_info(my_char):
    char_order = ord(my_char)
    if '0' <= my_char <= '9':
        char_type = "number"
    elif 'a' <= my_char <= 'z' or 'A' <= my_char <= 'Z':
        char_type = "letter"
    else:
        char_type = "punctuation"
    return my_char, char_order, char_type


if __name__ == '__main__':
    print(character_info("q"))
    print(character_info("7"))
    print(character_info("`"))
