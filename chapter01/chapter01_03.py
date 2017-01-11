#!/usr/bin/env python


def execute(x):
    templist = x.split(" ")
    ret = []
    for item in templist:
        num = 0
        for ch in item:
            if ch.isalpha():
                num = num + 1
        ret.append(num)
    return ret
