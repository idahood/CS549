#!/usr/bin/env python

import argparse
import math
from pprint import pprint


def is_not_pow2(n):
    if math.log(n, 2) is int:
        return True
    else:
        return False


def calc_parity(word):
    parity = 0
    while (2**parity < parity + len(word) + 1):
        parity += 1
    return parity


def gen_hamming_code(word, parity):
    code = [[9 for row in range(len(word) + parity + 1)] for col in range(parity)]
    check_bit = 0
    while check_bit < parity:
        i = 0
        while i < (len(word) + parity + 1):
            code[check_bit][i] = int(i / 2**check_bit) % 2
            i += 1
        check_bit += 1

    for word in code:
        word.pop(0)
    return code


def check_bits(data, code):
    result = []
    for word in code:
        c_x = 0
        for i in range(2**c_x, len(word)):
            if word[i] == 1:
                c_x = c_x ^ int(word[i])
        result.append(str(c_x))
    return result[::-1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sent_msg", help="the original message")
    parser.add_argument("rec_msg", help="the recieved message")
    args = parser.parse_args()

    parity = calc_parity(args.sent_msg)
    hc = gen_hamming_code(args.sent_msg, parity)
    print 'Hamming Code'
    pprint(hc)
    sent_syndrome = check_bits(args.sent_msg, hc)
    print 'Sent Syndrome'
    pprint(sent_syndrome)
    rec_syndrome = check_bits(args.rec_msg + ''.join(sent_syndrome), hc)
    print 'Rec Syndrome'
    pprint(rec_syndrome)

    for s1,s2 in zip(sent_syndrome,rec_syndrome):
        print int(s1) ^ int(s2)

if __name__ == '__main__':
    main()
