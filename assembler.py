#!/usr/bin/env python3

import sys

def main():
    parse_labels()

""" 
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
""" 

def parse_labels():
    linenum = 0
    with open("test.asm") as f:
        for line in f:
            line = line.strip().replace('\r', '') 
            # Comments
            if line[0] == '#':
                continue 
            if line[0] == '.':
                labels[line[1:]] = linenum*4 
            else:
                linenum += 1
    f.close() 


if __name__ == "__main__":
    main()
