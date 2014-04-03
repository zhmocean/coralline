import web
import router
import hashlib

class s_index:
    def GET(self, name):
        chip = name.split("/")
        print name
        newPlace = name.replace(chip[0], "", 1)
        #print newPlace
        newPlace = web.ctx.protocol+"://"+globals()["router"].getIpByType(chip[0])+newPlace
        #print newPlace
        web.redirect(newPlace)

class me_service:
    def GET(self):
        #ip from Front-Point header proxy
        return "Address: " +web.ctx.env.get("HTTP_X_REAL_IP")

class up_service:
    def GET(self):
        inputs = web.input()
        sig = inputs.get("sig")
        rand = inputs.get("rand")
        ip = inputs.get("ip")
        type_name = inputs.get("type")

        if (self.__checkPwd(sig, rand)):
            print globals()["router"]
            globals()["router"].changeIp(ip, type_name)

            return '{"result":"success"}'
        return '{"result":"failed", "message":"pwd error"}'

    def __checkPwd(self, sig, rand):
        #nowSig = hashlib.md5("mypassword"+rand).hexdigest().lower()
        #return nowSig == sig.lower()
        return "mypassword" == sig


class TinyWeb:
    def __init__(self):
        globals()["router"] = router.Router()
        self.app = web.application(self.__urls(), globals(), True)

    def __urls(self):
        return (
            '/up', 'up_service',
            '/me', 'me_service',
            '/(.+)', 's_index'
        )

    def start(self):
        self.app.run()

if __name__ == "__main__": 
    w = TinyWeb()
    w.start()