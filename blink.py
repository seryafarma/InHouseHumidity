import time
import network
from machine import Pin

period = 250
connected = False
print("Hello Network")

wlan_sta = network.WLAN(network.STA_IF)
wlan_sta.active(True)
if wlan_sta.isconnected():
    print("Already connected")
    connected = True
    period = 1000
ssid = ""
password = ""
print('Trying to connect to %s...' % ssid)

for retry in range(200):
    if connected:
        period = 1000
        break
    wlan_sta.connect(ssid, password)
    connected = wlan_sta.isconnected()
    
    time.sleep(1000)
    print('.', end='')

if connected:
    print('\nConnected. Network config: ', wlan_sta.ifconfig())
else:
    print('\nFailed. Not Connected to: ' + ssid)

print("Hello World")
p2 = Pin(2,Pin.OUT)

while True:
  p2.on()
  time.sleep_ms(period)
  p2.off()
  time.sleep_ms(period)
