from random import randint


def generate_alpha_string(length):
    return ''.join([chr(randint(65, 90)) for _ in range(length)])


def generate_num_string(length):
    return ''.join([str(randint(0, 9)) for _ in range(length)])


def generate_alphanum_string(length):
    string = []
    for n in range(length):
        num = randint(55, 90)  # A-Z with room for 0-9
        if num < 65:
            string.append(str(num - 55))
        else:
            string.append(chr(num))
    return ''.join(string)


def main():
    for n in range(20):
        print(generate_alpha_string(7))


if __name__ == '__main__':
    main()
