#!/usr/bin/python

import re

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

print (re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))
