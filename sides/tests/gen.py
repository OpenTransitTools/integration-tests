"""
simple utility that generate a bunch of .side files for use in automate.browserstack.com

"""
import os
import sys
from datetime import datetime

this_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(this_dir, '..')
smoke_dir = os.path.join(this_dir, 'smoke')

with open(filename, 'w') as f:
  pass

## json.load(file object)


for rec in browsers:
     write_cap_file(rec)
