import json,requests

class handler(object):
    def __init__(self,call,parseAPPID,parseRESTKey):
        self.call = call
        self.appid = parseAPPID
        self.restkey = parseRESTKey
    def send(self):
        headers= {"X-Parse-Application-Id": self.appid,
       "X-Parse-REST-API-Key": self.restkey}

        with open(self.call.mFile.name,'rb') as payload:
            h = requests.post("https://api.parse.com/1/files/callfile.mp3",headers=headers,data=payload)
        dataload = {"unitName":self.call.unit.name,"unitStationNumber":self.call.unit.stationNumber,"calldate":{"__type":"Date","iso":self.call.date.isoformat()},"callFile":{"name":h.json()["name"],"__type":"File"}}
        r = requests.post("https://api.parse.com/1/classes/Call",data=json.dumps(dataload),headers=headers)
        print r, r.text


