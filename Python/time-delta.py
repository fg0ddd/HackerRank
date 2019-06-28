#!/usr/bin/env python3
#Python3 deer bichsen
import datetime
#####################################################
def read_datetime():
    return datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')

def main():
    c = int(input())
    for i in range(c):
        tsag1 = read_datetime()
        tsag2 = read_datetime()
        
        print(int(abs(tsag1 - tsag2).total_seconds()))

if __name__ == '__main__':
main()
