def print_full_name(first, last):
    print("Hello {fname} {lname}! You just delved into python.".format(fname=first, lname=last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)