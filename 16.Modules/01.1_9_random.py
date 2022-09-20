
if __name__ == '__main__':
    # 1
    import random
    import string
    print('#1')
    print(f"chosen color is {random.randint(0,0xffffff)}")
    string1 = ''
    len1 = 12
    for i in range(0, len1):
        string1 += random.choice(string.ascii_letters)
    print('random string is :', string1)
    num1 = random.randint(-20, 60)
    num2 = random.randint(0, 356)
    print("random numbers are: ", num1, num2)
    num3 = random.randint(0, 70) * 7
    num4 = random.randrange(0, 70, 7)
    print('dividable by 7 nums are: ', num3, num4)

    # 2
    print('#2')
    import random
    list1 = [13, 42, [23, 45], 30, 'hell']
    el1 = random.choice(list1)
    print('random element from list:', el1)
    set1 = {12, 34, 56}
    # el2 = random.choice(set1)  #TypeError
    tuple1 = tuple(list1)
    el3 = random.choice(tuple1)
    print('random element from tuple:', el3)
    dict1 = {'name': 'rose', 'age': 12, 'nationality': 'England', 'class': 8 }
    key1 = random.choice(list(dict1))
    print('random element from dictionary: {}: {}'.format(key1, dict1[key1]))
    import os
    dirs = os.listdir(r'C:\Users\Saeid\Desktop\Training\Python')
    print(os.getcwd())
    print(random.choice(dirs))

    # 3
    print('#3')
    import random
    import string
    letters = string.ascii_letters
    char1 = random.choice(letters)
    print('random letter:', char1)
    string2 = ''
    max_length = 200
    string_len = random.randint(0, max_length)
    for i in range(0, string_len):
        string2 += random.choice(letters)
    print(f'random string with length {string_len}:', string2)
    string2 = ''
    for i in range(20):
        string2 += random.choice(letters)
    print('random string with length 20:', string2)

    # 4
    print('#4')
    print('random num:', random.Random().random())
    print('seeded random num:', random.Random(0).random())
    random.seed(1)
    print('seeded random num:', random.random())
    import time
    random.seed(time.time())
    print('seeded random num:', random.random())

    # 5
    print('#5')
    import random
    print(random.randrange(5))
    print(random.randrange(5, 10))
    print(random.randrange(stop=10, start=5, step=3))
    import datetime
    birth_date = datetime.date(1995, 3, 14)
    current_date = datetime.date.today()
    date_difference = (current_date - birth_date).days
    random_days = random.randrange(date_difference)
    random_date = birth_date + datetime.timedelta(days=random_days)
    print(random_date)

    # 6
    print('#6')
    import random
    import string
    letters = list(string.ascii_letters)
    random.shuffle(letters)
    print(''.join(letters))

    # 7
    print('#7')
    import random
    print(random.uniform(0, 1))
    print(random.uniform(2, 5.68))

    # 8
    print('#8')
    import random
    population = range(10, 120, 3)
    print(random.sample(population, 8))

    # 9
    print('#9')
    import random
    random.seed(1)
    print(random.random())
    random.seed(4)
    print(random.random())
    random.seed(8)
    print(random.random())
    import time
    random.seed(time.time())
    print(random.random())