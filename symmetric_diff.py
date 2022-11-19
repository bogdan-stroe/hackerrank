if __name__ == '__main__':
    N = int(input())
    nElems = input().split()
    nInts =  list(map(int, nElems))
    nSet = set(nInts)
    M = int(input())
    mElems = input().split()
    mInts =  list(map(int, mElems))
    mSet = set(mInts)
    symDiff = nSet.symmetric_difference(mSet)
    result = list(symDiff)
    result.sort()
    for i in result:
        print(i)
