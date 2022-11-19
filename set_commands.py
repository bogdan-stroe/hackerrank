if __name__ == '__main__':
    n = int(input())
    mySet = set(map(int, input().split()))
    m = int(input())
    for i in range(m):
        commands = input().split()
        command = commands[0]
        if command == 'pop':
            try:
                mySet.pop()
                #print(mySet)
            except KeyError:
                pass
        elif command == 'remove':
            try:
                mySet.remove(int(commands[1]))
            except KeyError:
                pass
        elif command == 'discard':
            mySet.discard(int(commands[1]))
    
    print(sum(mySet))