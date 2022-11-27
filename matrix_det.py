import numpy

def main():
    size = int(input())
    matrix = []
    for i in range(size):
        line = list(map(float, input().split()))
        matrix.append(line)
    print(round(numpy.linalg.det(matrix), 2))

if __name__ == '__main__':
    main()