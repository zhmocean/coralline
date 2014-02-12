__author__ = 'Administrator'

import yaml

class Router:
    def __init__(self):
        self.ips = self.__loadIps()

    def __loadIps(self):
        f = file("ip_resolve.conf", "r")
        c = yaml.load(f)
        f.close()

        return c

    def getIpByType(self, type_name):
        return self.ips.get(type_name)

    def changeIp(self, ip, type_name):

        f = file("ip_resolve.conf", "r")
        c = yaml.load(f)
        f.close()

        if not c:
            c = {}

        if((c.get(type_name) != ip)):
            c[type_name] = ip
            self.ips = c

            f = file("ip_resolve.conf", "w")
            yaml.dump(c, f)
            f.close()