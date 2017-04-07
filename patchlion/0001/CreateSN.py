# -*- coding: utf-8 -*-
__author__ = 'PatchLion'
import uuid

def createSN(count):
    if count <= 0:
        return


    sns=[]

    for i in range(count):
        sns.append(uuid.uuid4().hex.upper())

    return sns

def createSNAndSaveToFile(count, filepath):
    sns = createSN(count)

    with open(filepath, 'wt') as f:
        for sn in sns:
            f.write(sn+"\n");

print(createSN(200))
createSNAndSaveToFile(200, 'sns.txt')