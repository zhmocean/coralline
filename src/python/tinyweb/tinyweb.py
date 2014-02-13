import web
import yaml
import router

class s_index:
    def GET(self, name):
        chip = name.split("/")
        print name
        newPlace = name.replace(chip[0], "", 1)
        #print newPlace
        newPlace = web.ctx.protocol+"://"+globals()["router"].getIpByType(chip[0])+newPlace
        #print newPlace
        web.redirect(newPlace)


class up_service:
    def GET(self):
        inputs = web.input()
        pwd = inputs.get("password")
        ip = inputs.get("ip")
        type_name = inputs.get("type")

        if (self.__checkPwd(pwd)):
            print globals()["router"]
            globals()["router"].changeIp(ip, type_name)

            return '{"result":"success"}'
        return '{"result":"failed", "message":"pwd error"}'

    def __checkPwd(self, pwd):
        return pwd == "mypassword"


class TinyWeb:
    def __init__(self):
        globals()["router"] = router.Router()
        self.app = web.application(self.__urls(), globals(), True)

    def __urls(self):
        return (
            '/(.+)', 's_index',
            '/up', 'up_service'
        )

    def start(self):
        self.app.run()

if __name__ == "__main__": 
    w = TinyWeb()
    w.start()