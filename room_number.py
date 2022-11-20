def main():
    size = int(input())
    rooms = input().split()
    countRooms = {}
    for elem in rooms:
        if elem in countRooms:
            countRooms[elem] = countRooms[elem] + 1
        else:
            countRooms[elem] = 1
    for roomNum in countRooms:
        if countRooms[roomNum] == 1:
            print(roomNum)
            break

if __name__ == '__main__':
    main()
