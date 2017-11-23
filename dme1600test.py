'''
dme1600test.py
MIT License
Copyright (c) 2017 Shimbo
'''

import usbtmc


inst = usbtmc.Instrument(0x0b3e, 0x1026 )
data = inst.ask("*IDN?")
print(data)
inst.close()
