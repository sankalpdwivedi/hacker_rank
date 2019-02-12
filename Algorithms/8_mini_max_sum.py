
#!/bin/python

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr = sorted(arr)
    print sum(arr[:-1]), sum(arr[1:])


if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
