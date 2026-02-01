# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import argparse
from collections import Counter
from itertools import islice

def main(file: str) -> dict:
    try:
        with open(file, 'r') as f:
            status = [i.split()[-4] for i in f.readlines()]
        return dict(islice(Counter(status).items(), 3))
    except FileNotFoundError:
        print(f"Error: {file} not found")
        return dict()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Parse Nginx status codes')
    parser.add_argument('file', nargs='?', default='./access.log', help='Log File Path')
    args = parser.parse_args()

    for key,value in main(args.file).items():
        print(f'{key}: {value}')