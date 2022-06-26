#!/usr/bin/env python3

import sys
import re 

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
            # Ignore Comments
            if line[0] == '#':
                continue 
            if line[0] == '.':
                labels[line[1:]] = linenum*4 
            else:
                linenum += 1
    f.close() 


def check_tokens():
    with open("test.asm") as f:
        for line in f:
            if line[0] == '.':      # Ignore labels 
                continue

            if line[0] == '#':      # Ignore comments
                continue        

            line = line.strip().replace('\r', '') 
            token = re.split(r'[, ]', line)

            if '' in token: 
                token.remove('') 

            if token[0] == "ld":
                r0 = int(token[1]) 
                if r0 >= 0 and r <= 7: 
                    a0 = token[2] 
                    if a0[0] == '$':   # Address
                        addr = int(a0[1:], 0) 
                        b = [0x02, r, addr >> 8, addr & 0xFF] 





if __name__ == "__main__":
    main()
