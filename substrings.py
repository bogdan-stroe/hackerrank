def merge_the_tools(string, k):
    assert(len(string)%k == 0)
    subs =[]
    for i in range(len(string)//k):
        subs.append(string[i*k: (i+1)*k])
    results = []
    for sub in subs:
        res = ''
        for a in sub:
            if a not in res:
                res += a
        results.append(res)
    for item in results:
        print(item)

if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)