def main():
    rounds = int(input())
    for i in range(rounds):
        aSize = int(input())
        aSet = set(map(int, input().split()))
        bSize = int(input())
        bSet = set(map(int, input().split()))
        print(aSet.issubset(bSet))


if __name__ == '__main__':
    main()