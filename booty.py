import time
import adafruit_bmp280
from machine import Pin, I2C


# Create library object using our Bus I2C port
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
adress = i2c.scan()
print(adress)

try:
  bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c=i2c)
  # change this to match the location's pressure (hPa) at sea level
  bmp280.sea_level_pressure = 1013.25
  
  print(bmp280.temperature) 
  print(bmp280.temperature) 

except OSError as e:
  print('Failed to read')
