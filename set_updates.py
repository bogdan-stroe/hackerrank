def main():
    size = int(input())
    mySet = set(map(int, input().split()))
    num = int(input())
    for i in range(num):
        oper = input().split()
        command = oper[0]
        newSet = set(map(int, input().split()))
        if command == 'intersection_update':
            mySet.intersection_update(newSet)
        elif command == 'update':
            mySet.update(newSet)
        elif command == 'symmetric_difference_update':
            mySet.symmetric_difference_update(newSet)
        elif command == 'difference_update':
            mySet.difference_update(newSet)
    print(sum(mySet))

if __name__ == '__main__':
    main()