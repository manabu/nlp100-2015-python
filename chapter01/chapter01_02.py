#!/usr/bin/env python
# hint: zip list flatten iterable
# python2 reduce

def execute(x,y):
    templist = list(zip(x,y))
    ret = []
    for item in templist:
        ret.extend(item)
    return "".join(ret)
