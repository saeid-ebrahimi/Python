

class Number:
    def __init__(self, num_value, num_even, num_enrolled=False):
        self.value = num_value
        self.even = num_even
        self.enrolled = num_enrolled


if __name__ == "__main__":
    value = 101
    even = False
    number_instance = Number(value, even)

