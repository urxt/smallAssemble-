#!/usr/bin/env python3

import sys

def main():
    check_file("test.asm")

def check_file(filename): 
    file = open(filename)
    for lines in file: 
        print(lines.strip())

if __name__ == "__main__":
    main()
