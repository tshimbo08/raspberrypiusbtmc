import usbtmc

inst = usbtmc.Instrument(0x0b3e, 0x1026 )
data = inst.ask("*IDN?")
print(data)
inst.close()
