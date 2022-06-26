#!/usr/bin/env python3

import sys

def main():
    check_file("test.asm")

def check_file(filename): 
    file = open(filename)
    for lines in file: 
        tokens = lines.split(' ')
        if(tokens[0]) == "ld":
            print("LOAD instruction")
        elif(tokens[0]) == "add":
            print("ADD instruction")
        elif(tokens[0]) == "sd":
            print("STORE instruction")

if __name__ == "__main__":
    main()
