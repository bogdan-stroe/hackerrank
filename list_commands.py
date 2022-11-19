if __name__ == '__main__':
    N = int(input())
    myList = []
    for i in range(N):
        args = input().split(' ')
        command = args[0]
        if command == 'print':
            print(myList)
        elif command == 'insert':
            index = int(args[1])
            elem = int(args[2])
            myList.insert(index, elem)
        elif command == 'remove':
            elem = int(args[1])
            myList.remove(elem)
        elif command == 'append':
            elem = int(args[1])
            myList.append(elem)
        elif command == 'sort':
            myList.sort()
        elif command == 'pop':
            myList.pop()
        elif command == 'reverse':
            myList.reverse()

