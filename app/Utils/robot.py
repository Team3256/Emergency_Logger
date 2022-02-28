from networktables import NetworkTables
import Utils.config as cf

NetworkTables.initialize(server=cf.BOT_IP)
sd = NetworkTables.getTable(cf.TABLE_NAME)

def getLog(key):
    return sd.getString(key, "No Logs Available.")

def getLogKeys():
    return sd.getKeys()

def putLog(key, log):
    sd.putString(key, log)