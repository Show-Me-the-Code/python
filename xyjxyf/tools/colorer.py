# coding = utf-8

import random

def randRGB(min=0, max=255):
    if min < 0:
        min = 0
    if min > 255:
        min = 255

    if max < 0:
        max = 0
    if max > 255:
        max = 255

    if max < min:
        tmp = min
        min = max
        max = tmp

    return (random.randint(min, max),
           random.randint(min, max),
           random.randint(min, max))

