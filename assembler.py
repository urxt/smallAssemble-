#!/usr/bin/env python3
import sys
def main():
    tokens = []
    with open("test.asm", 'r') as f:
        for line in f.read():
            tokens = line.split()
            for i in tokens: 
                print(i)


if __name__ == "__main__":
    main()
