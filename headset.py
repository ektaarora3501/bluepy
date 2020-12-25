# connecting headphones with bluetooth using python
from bluetooth import *
from pprint import pprint

# checking available devices
device = discover_devices(lookup_names=True, lookup_class=True)


def connect(addr, port):
    sock = BluetoothSocket(RFCOMM)
    sock.connect((addr, port))
    sock.close()


final_add = None
print(device)
for addr, name, _ in device:
    if name == 'HD 350BT':
        final_add = addr
        break

if final_add != None:
    service = find_service(address=final_add)
    pprint(service)
    a = service[0]
    print(a['port'], a['host'])
    connect(a['host'], a['port'])

else:
    print("no device detected with that name")
