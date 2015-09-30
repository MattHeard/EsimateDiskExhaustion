#!/usr/bin/python3

from sys import stdin


def estimateConf(conf):
    """Estimate configuration from a string."""
    confElements = [int(x) for x in conf.split(sep=" ")]
    disk = confElements[0]
    print(disk)
    procRates = confElements[1:]
    print(procRates)

def estimateConfsFromInput():
    """Parse and estimate configurations from stdin."""
    for line in stdin:
        confs = line.splitlines()
        for conf in confs:
            estimateConf(conf)

if __name__ == "__main__":
    estimateConfsFromInput()
