# raspberrypiusbtmc
Using usbtmc for Raspberry Pi3

# first step
Install the library.
```console
 $ sudo pip3 install pyUSB
 $ sudo pip3 install python-usbtmc
```

Make group.
```console
 $ sudo groupadd usbtmc
 $ sudo usermod -aG usbtmc pi
```

Make usbtmc.rules at /etc/udev/rules.d/
```
 #USB TMC instrument
 #DME1600
 SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idVendor}=="0b3e", ATTRS{idProduct}=="1026",GROUP="usbtmc", MODE="0660"
 KERNEL=="usbtmc/*",       MODE="0660", GROUP="usbtmc"
 KERNEL=="usbtmc[0-9]*",   MODE="0660", GROUP="usbtmc"
```

