"""
This example shows how to verify a previously saved fingerprint.
"""

import fprint
import os
# Initialization of libfprint
fprint.init()

os.system("sudo chmod a+rw /dev/bus/usb/001/004")
# Load fingerprint info from a binary file (see enroll.py)
with open('/home/pi/Fingerprint_Contact_Tracing/fingerprint_data.bin', 'rb') as fh:
    print(type(fh))
    fingerprint = fprint.PrintData.from_data(fh.read())

print(type(fingerprint))
# Discover all fingerprint devices in the system
# ddevs: Sequence[fprint.DiscoveredDevice]
ddevs = fprint.DiscoveredDevices()
if len(ddevs) > 0:
    # Choose the first one
    # dev: fprint.Device
    dev = ddevs[0].open_device()

    # Start fingerprint verification. In that moment you should 
    # place your finger on the device.
    # matched: bool 
    matched = dev.verify_finger_loop(fingerprint)

    if matched:
        print("Welcome Andrew Stephen!")
    else:
        print("Get out, I don't know you...")

    dev.close()

fprint.exit()

