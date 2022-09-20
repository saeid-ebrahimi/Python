

if __name__ == "__main__":
    myString = "This is the string whose words we would like to count. \
    This string contains some repeated words, as well as some unique words. \
    It contains punctuation, and it contains words that are capitalized in different ways. \
    If the method we write runs correctly, it will count 4 instances of the word 'it', \
    3 instances of the word 'this', and 3 instances of the word 'count'."

    myString = myString.lower()
    myString = myString.replace(',', '')
    myString = myString.replace('.', '')
    myString = myString.replace("'", "")
    myString_list = myString.split()
    my_dic = {}
    for word in myString_list:
        if word not in my_dic:
            my_dic[word] = 0
        my_dic[word] += 1
    print(my_dic)
