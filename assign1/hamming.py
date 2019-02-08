#!/usr/bin/env python

import argparse


def hamming(string1, string2):
    distance = 0
    for s1, s2 in zip(string1, string2):
        if s1 != s2:
            distance += 1
    return distance


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("string1", help="string1")
    parser.add_argument("string2", help="string2")
    args = parser.parse_args()

    print hamming(args.string1, args.string2)


if __name__ == '__main__':
    main()
