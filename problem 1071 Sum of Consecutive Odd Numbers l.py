def main():
    X = int(input())
    Y = int(input())
    start = min(X,Y)+1
    end = max(X,Y)
    if start % 2 == 0:
        start += 1

    sum = 0
    for i in range(start, end, 2):
        sum += i
    print(sum)
if __name__ == '__main__':
    main()