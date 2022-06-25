#!/usr/bin/env python3

import sys

def main():
    token = list()
    with open("test.asm", 'r') as f:
        for line in f.read():
            token = line.split()
    f.close()
    

if __name__ == "__main__":
    main()
