from __future__ import print_function
import os
from PIL import Image

size = (128,128)

all_files = os.listdir(os.curdir)
for infile in all_files:
    outfile = os.path.splitext(infile)[0] + '.thumbnail'
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, 'JPEG')
        except IOError:
            print('cannot create thumbnail for', infile)
