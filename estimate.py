#!/usr/bin/python3

from sys import stdin

def calcExhaustion(disk, procRates):
    """Calculate how many seconds before the disk is filled.
       
       procRates lists the rates at which each process fills 1 byte of disk
       space."""
    eta = 0;
    while disk > 0:
        eta += 1
        for rate in procRates:
            if eta % rate == 0:
                disk -= 1
    return eta

def estimateConf(conf):
    """Estimate configuration from a string."""
    confElements = [int(x) for x in conf.split(sep=" ")]
    disk = confElements[0]
    procRates = confElements[1:]
    eta = calcExhaustion(disk, procRates);
    print(eta)

def estimateConfsFromInput():
    """Parse and estimate configurations from stdin."""
    for line in stdin:
        confs = line.splitlines()
        for conf in confs:
            estimateConf(conf)

if __name__ == "__main__":
    estimateConfsFromInput()
