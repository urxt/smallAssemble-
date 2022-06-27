#!/usr/bin/env python3

import sys
import re 

def main():
    check_tokens()

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

def write_to_binary(text): 
    with open("test.bin", 'a+b') as f:
        f.write(bytearray(text))
        f.close()

def zero_to_binary():
    with open("test.bin", 'w+b') as f:
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
                r = int(token[1][1]) 
                if r >= 0 and r <= 7: 
                    a0 = token[2] 
                    if a0[0] == '$':            # Address
                        addr = int(a0[1:], 0) 
                        b = [0x02, r, addr >> 8, addr & 0xFF] 
                        write_to_binary(b)

                    elif a0[0] == 'R':          # Register
                        r1 = int(a0[1:], 0) 
                        b = [0x01, r, 0, r1]
                        write_to_binary(b) 

                    else:
                        v = int(a0, 0)          # Value 
                        b = [0x00, r, v >> 8, v & 0xFF] 
                        write_to_binary("test.bin", b) 

                else:
                    print("Invalid reg name")
                    print(token[1])
                    sys.exit()

            elif token[0] == "sd":
                r = int(token[1][1]) 
                if r >= 0 and r <= 7: 
                    a0 = token[2] 
                    if a0[0] == '$':            # Address
                        addr = int(a0[1:], 0) 
                        b = [0x10, r, addr >> 8, addr & 0xFF] 
                        write_to_binary(b)

                    elif a0[0] == 'R':          # Register
                        r1 = int(a0[1:], 0) 
                        b = [0x13, r, 0, r1]
                        write_to_binary(b) 

                    else:
                        print("Invalid Mode") 
                        print(line)
                        sys.exit()

                else:
                    print("Invalid reg name") 
                    print(token[1])
                    sys.exit()


if __name__ == "__main__":
    main()
