def load(filename):
    in_file = open(filename, "r")
    line = in_file.readline().strip()
    in_file.close()

    if line.find('-') == 0:
        line_temp = line.replace('-', '')
        if '.' in line_temp:
            line_temp = line_temp.replace('.', '')
            print(line_temp)
            if line_temp.isdecimal():
                return float(line)
        elif line_temp.isdecimal():
            return int(line)
        else:
            return line
    else:
        if '.' in line:
            line_temp = line.replace('.', '')
            if line_temp.isdigit():
                return float(line)
        elif line.isdecimal():
            return int(line)
        else:
            return line


if __name__ == '__main__':
    file = load("read_input_file.txt")
    print(file)
    print(type(file))
