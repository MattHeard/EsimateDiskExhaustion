#!/usr/bin/python3

from sys import stdin

def estimateConf(conf):
    print(conf)

def estimateConfsFromInput():
    for conf in stdin:
        estimateConf(conf)

if __name__ == "__main__":
    estimateConfsFromInput()
