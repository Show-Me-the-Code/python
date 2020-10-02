#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:jackiedabekar<deepakvdabekar@gmail.com>
# File:key_generator.py
# Create Date: 02-10-2020
# Description: Using random and string to generate 200 register keys
# Usage: key_generator.py

from random import choice
from string import ascii_letters, digits

def generate(num_of_password, length_of_each_password):
	creator = ascii_letters + digits
	for password in range(num_of_password):
		Re = ''
		for per_pass in range(length_of_each_password):
			Re += choice(creator)
		print(Re)


num_of_password = int(input('Enter Number Of Password You Want: '))
len_of_each = int(input('Length of Ecah Password Must Be: '))

generate(num_of_password, len_of_each)
print('All Password Generated Successfully')
		
