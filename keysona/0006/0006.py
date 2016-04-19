#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: key
# @Date:   2015-11-17 17:32:09
# @Last Modified by:   key
# @Last Modified time: 2015-11-17 19:02:54

import os
import glob
from collections import Counter

def main():
    os.chdir('data')
    texts = glob.glob("*.txt")

