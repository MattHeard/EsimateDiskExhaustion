#!/usr/bin/python3

from sys import stdin

def estimateConf(conf):
    print(conf)

def estimateConfsFromInput():
    for line in stdin:
        confs = line.splitlines()
        for conf in confs:
            estimateConf(conf)

if __name__ == "__main__":
    estimateConfsFromInput()
