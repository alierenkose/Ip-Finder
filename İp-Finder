###@alierenkose

import socket
import urllib.request

# Get Local IP Address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
s.close()
print("Local IP: ", local_ip)

# Get Public IP Address
try:
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
except:
    external_ip = "Not Found!"

print("Public IP:", external_ip)


###@alierenkose
