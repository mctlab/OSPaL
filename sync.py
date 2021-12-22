#!/usr/bin/env python
#coding=utf-8

import os
from datetime import date

os.system('git add .')
today = date.today()
commitMessage = 'SYNC-' + today.isoformat()
os.system('git commit -m "' + commitMessage + '"')
os.system('git push')
