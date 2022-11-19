if __name__ == '__main__':
    args = input().split()
    sizes = list(map(int, args))
    args = input().split()
    target = list(map(int, args))
    args = input().split()
    positive = set(map(int, args))
    args = input().split()
    negative = set(map(int, args))
    #assert input is valid
    assert sizes[0] == len(target)
    assert sizes[1] == len(positive)
    assert sizes[1] == len(negative)
    assert len(positive.intersection(negative)) == 0

    score = 0
    for elem in target:
        if elem in positive:
            score = score + 1
        elif elem in negative:
            score = score -1
    print(score) 

