__author__ = 'Administrator'

import yaml

class Router:
    def __init__(self):
        self.table = self.__loadTable()

    def __loadTable(self):
        c = None

        try:
            f = file("ip_resolve.conf", "r")
            c = yaml.load(f)
        except:
            pass
        finally:
            f.close()

        if not c:
            c = {}

        return c

    def getIpByType(self, type_name):
        return self.table.get(type_name)["ip"]

    def getConfigByType(self, type_name):
        return self.table.get(type_name)

    def changeIp(self, ip, type_name, port="80"):
        c = self.__loadTable()

        if(not c.get(type_name)) or (c.get(type_name)["ip"] != ip) or (c.get(type_name)["port"] != port):
            c[type_name] = {}
            c[type_name]["ip"] = ip
            c[type_name]["port"] = port
            self.table = c

            f = file("ip_resolve.conf", "w")
            yaml.dump(c, f)
            f.close()
