if __name__ == '__main__':
    size = int(input())
    countries = set()
    for i in range(size):
        countries.add(input())
    print(len(countries))