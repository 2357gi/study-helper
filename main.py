# coding=utf-8

import pyperclip

path = 'drills.md'
with open(path) as f:
    l_strip = [s.strip() for s in f.readlines()]

print('READY!!')

text = pyperclip.paste()
while(1):
    if text != pyperclip.paste():
        text = pyperclip.paste()
        print("\n「", text,'」')
        for line in l_strip:
            if text in line:
                print('   >> ',line)
