
# !/bin/python

# Complete the staircase function below.
def staircase(n):
    hashes = 1
    spaces = n - hashes
    while spaces >= 0:
        print "{}{}".format(" " * spaces, "#" * hashes)
        hashes += 1
        spaces = n - hashes


if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
