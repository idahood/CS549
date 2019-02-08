#!/usr/bin/env python

import hamming

def main():
    code = [
            '000111',
            '111000',
            '000000']

    hd_of_code = len(code[0])
    for a_iter in code:
        for b_iter in code:
            if a_iter != b_iter:
                ab_result = hamming.hamming(a_iter, b_iter)
                if ab_result < hd_of_code:
                    hd_of_code = ab_result

    print hd_of_code


if __name__ == '__main__':
    main()
