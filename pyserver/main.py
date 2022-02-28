import time
from networktables import NetworkTables

NetworkTables.initialize(server='10.32.56.2')

sd = NetworkTables.getTable("Logs")

