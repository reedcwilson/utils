#!/usr/bin/env python

import os
import sys
from glob import glob

files = [y for x in os.walk('.') for y in glob(os.path.join(x[0], '*.*'))]

for filename in files:
  contents = None
  with open(filename, 'r') as f:
    contents = f.read()
  print "%d carriage returns erased in %s" % (contents.count('\r'), filename)
  with open(filename, 'w') as f:
    f.write(contents.replace('\r', ''))
