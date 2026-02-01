# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sys
from collections import Counter
from itertools import islice

def main(file: str) -> dict:
    with open(file, 'r') as f:
        status = [i.split()[-4] for i in f.readlines()]
    return dict(islice(Counter(status).items(), 3))

if __name__ == '__main__':
    file = sys.argv[1]
    for key,value in main(file).items():
        print(f'{key}: {value}')