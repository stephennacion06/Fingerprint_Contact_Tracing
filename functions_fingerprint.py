from db_modules import insertdata, convertToBinaryData, \
                        writeTofile, get_fingerprint_data, \
                        get_list_fingerprint
import fprint
import datetime
import os


os.system("sudo chmod a+rw /dev/bus/usb/001/003")

# fingerprint = convertToBinaryData("some_fingerprint.bin")

def enroll_fingerprint():
    fprint.init()
    ddevs = fprint.DiscoveredDevices()
    
    if len(ddevs) > 0:
    
        # Choose the first one
        # dev: fprint.Device
        dev = ddevs[0].open_device()
        
        # print_data: Optional[fprint.PrintData]
        print_data = dev.enroll_finger_loop()
        
        if print_data is None:
            print("Fail")
        else:
            print("Success")

            # Persist fingerprint info
            with open("fingerprint_data.bin", "wb") as fh:
                fh.write(print_data.data)

        dev.close()

    fprint.exit()
    

def enroll_prompt():
    
    name = input("Name: ")
    email = input("Email: ")
    address = input("Address: ")
    gender = input("Gender: ")
    phone = input("Phone #: ")
    location_record = input("Current Location: ")
    
    print("Please input 5 fingerprints")
    
    enroll_fingerprint()
    fingerprint = convertToBinaryData("fingerprint_data.bin")
    
    insertdata(name, email, address, gender, phone, 
               location_record, datetime.datetime.now(), fingerprint)

def verify_fingerprint():
    
    fprint.init()

    ddevs = fprint.DiscoveredDevices()

    def ready_fingerprint_list():
        f_list = []
        
        fingerprint_list = get_list_fingerprint()
        print(len(fingerprint_list))
        print("Loading the Contact Tracing Database")
        
        for num in range(0,len(fingerprint_list)):
            fingerprint = fprint.PrintData.from_data(fingerprint_list[num])
            f_list.append(fingerprint)
        return tuple(f_list)

    fingerprint_list = ready_fingerprint_list()
    print(fingerprint_list)
    if len(ddevs) > 0:
        # Choose the first one
        # dev: fprint.Device
        dev = ddevs[0].open_device()

        # Start fingerprint verification. In that moment you should 
        # place your finger on the device.
        # matched: bool 
        
        matched, i, num = dev.identify_finger_img(fingerprint_list)
        
        if num != None:
            dev.close()

            fprint.exit()
            
            personal_data = get_fingerprint_data(num+1)
            print("-"*20,"WELCOME! ",personal_data[0],"-"*20)
            print(personal_data)
            return personal_data[0],num+1
            
        else:

            dev.close()

            fprint.exit()
            
            return False

# def enroll_fingerprint(name, email, address, gender, phone,  location_record):
    
#     try:
        
#         enroll_fingerprint()
        
#         fingerprint = convertToBinaryData("fingerprint_data.bin")
        
#         insertdata(name, email, address, gender, phone, 
#                 location_record, datetime.datetime.now(), fingerprint)
        
#         return True
    
#     except:
        
#         return False
        
    
    
    

# enroll_prompt()

#verify_fingerprint()