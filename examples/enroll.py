"""
This example shows you how to save a fingerprint to a file.
"""
import fprint

# Initialization of libfprint
fprint.init()


# Discover all fingerprint devices in the system
# ddevs: Sequence[fprint.DiscoveredDevice]
ddevs = fprint.DiscoveredDevices()
print(len(ddevs))
if len(ddevs) > 0:
    
    # Choose the first one
    # dev: fprint.Device
    dev = ddevs[0].open_device()
    print("Done Here")
    # print_data: Optional[fprint.PrintData]
    print_data = dev.enroll_finger_loop()
    print("These is here")
    if print_data is None:
        print("Fail")
    else:
        print("Success")

        # Persist fingerprint info
        with open("fingerprint_data.bin", "wb") as fh:
            fh.write(print_data.data)

    dev.close()

fprint.exit()
