import time
from networktables import NetworkTables
import constants as k

NetworkTables.initialize(server='10.32.56.2')

sd = NetworkTables.getTable("Logs")

i = 0
while True:
    print("robotTime:", sd.getNumber("robotTime", -1))

    sd.putNumber("robotTime", i)
    time.sleep(1)
    i += 1