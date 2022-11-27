def main():
    aSet = set(map(int, input().split()))
    aLen = len(aSet)
    isSuperset = True
    nOther = int(input())
    for i in range(nOther):
        oSet = set(map(int, input().split()))
        if aLen > len(oSet) and aSet.issuperset(oSet):
            pass
        else:
            isSuperset = False
    print(isSuperset)

if __name__ == '__main__':
    main()