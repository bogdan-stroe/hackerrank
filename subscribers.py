def main():
    fSize = int(input())
    french = set(input().split())
    assert fSize == len(french)
    eSize = int(input())
    english = set(input().split())
    assert eSize == len(english)
    subscribers = french.union(english)
    print(len(subscribers))


if __name__ == '__main__':
    main()