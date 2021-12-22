#!/usr/bin/env python3

import os
from datetime import date

files = os.listdir('.')
print(f'current: {os.getcwd()}')
dirs = []
for file in files:
    if os.path.isdir(file) and (not file.startswith('.')):
        dirs.append(file)

for index, dir in enumerate(dirs):
    print(f'[{index}] {dir}')

indexSelected = input('select directory [?]: ')
if not indexSelected.isdigit():
    print(f'[{indexSelected}] is invalid')
    quit(1)

index = int(indexSelected)
if (index >= len(dirs)):
    print(f'[{index}] is invalid')
    quit(1)

notebook = dirs[index]
today = date.today()
timePath = today.strftime('%Y-%m')
fileName = input('create note under %s/%s: ' % (notebook, timePath))

if len(fileName.strip()) == 0:
    print('fileName is blank')
    quit(1)

noteDir = os.path.join(notebook, timePath)
if not os.path.isdir(noteDir):
    os.makedirs(noteDir)
dayPrefix = today.strftime('%d')
fileName = '%s_%s.md' % (dayPrefix, fileName)
notePath = os.path.join(noteDir, fileName)

if os.path.isfile(notePath):
    print('file already exists')
    quit(1)

file = open(notePath, 'w')
file.close()

print(f'create note {notebook}/{timePath}/{fileName}')
