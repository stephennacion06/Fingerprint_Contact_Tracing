import fprint
import pickle

fprint.init()
devices = fprint.DiscoveredDevices()
fprint_list = []

if len(devices) > 0:
    dev = devices[0].open_device()
    
    print_data = dev.enroll_finger_loop()
    print("done scanning")
    
    print_data = fprint.PrintData.from_data(print_data.data)
    print(print(type(print_data)))
    fprint_list.append(print_data)
    with open('fprint.pickle', 'wb') as f:
        pickle.dumps(fprint_list, f)
        
    print_data = dev.enroll_finger_loop()
    print("done scanning")
    print_data = fprint.PrintData.from_data(print_data.data)
    print(print(type(print_data)))
    fprint_list.append(print_data)
    
    fprint_list = tuple(fprint_list)
    print(fprint_list)
    
    result = dev.identify_finger_img(fprint_list)
    print(result)
    dev.close()
