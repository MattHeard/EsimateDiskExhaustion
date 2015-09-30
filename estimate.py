#!/usr/bin/python3

from sys import stdin

def estimateConf(conf):
    confElements = [int(x) for x in conf.split(sep=" ")]
    disk = confElements[0]
    print(disk)
    procRates = confElements[1:]
    print(procRates)

def estimateConfsFromInput():
    for line in stdin:
        confs = line.splitlines()
        for conf in confs:
            estimateConf(conf)

if __name__ == "__main__":
    estimateConfsFromInput()
