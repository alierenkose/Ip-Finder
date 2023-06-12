###@alierenkose

import socket
import urllib.request

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
s.close()
print("Local IP: ", local_ip)

try:
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
except:
    external_ip = "Not Found!"


print("Public IP:", external_ip)

try:
    info = urllib.request.urlopen('https://ident.me/json').read().decode('utf8').split(',')
except:
    info = "Not Found!"

print("Country:", info[5].split(':')[1].split('"')[1])
print("City:", info[6].split(':')[1].split('"')[1])
print("Isp:", info[1].split(':')[1].split('"')[1])


###@alierenkose
