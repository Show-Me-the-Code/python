#Solution to problem 0001

'''
# Question 0001: As an independent developer of the Apple Store App, do you want to make a promotion, generate an activation code (or coupon)
# for your application , and how does Python generate
#  200 activation codes (or coupons)
'''

import string
import random
from sets import Set

numberOfActivationCodes = 200
lengthOfActivationCodes = 20

def getAllSymbols():
    return string.letters + string.digits

allSymbolsString = getAllSymbols()

def printActivationCodes():
    activationCodes = Set([])
    while len(activationCodes) < numberOfActivationCodes:
        lenOfString = 0
        currString = ""
        for i in range(0,len(allSymbolsString)):
            probability = random.random()
            if probability > 0.5:
                currString = currString + allSymbolsString[i]
            if(len(currString) == lengthOfActivationCodes):
                activationCodes.add(currString)
                break

    for i in activationCodes:
        print i


if __name__ == "__main__":
    printActivationCodes()