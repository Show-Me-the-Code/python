#!/usr/bin/env python3
import uuid

for i in range (0, 20):
    id = uuid.uuid4()
    print('i >> {0}, uuid >>> {1}'.format(i, id))
