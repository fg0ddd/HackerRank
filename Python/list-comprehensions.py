#!/bin/python2.7


if __name__ == '__main__':
    x = int(raw_input())+1
    y = int(raw_input())+1
    z = int(raw_input())+1
    n = int(raw_input())
    lst = [[i,j,k] for i in range(x) for j in range(y) for k in range(z) if i+j+k != n]
    print lst
