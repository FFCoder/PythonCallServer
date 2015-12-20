import json
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from models import *
from ParseHandler import handler


watchFolder = ""
parseAppId = ""
parseRESTKey = ""

class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.wav","*.mp3"]


    def on_created(self, event):
        print "New Call Found"
        filepath = event.src_path.encode('ascii','ignore')
        x = Call(open(filepath))
        handle = handler(x,parseAppId,parseRESTKey)
        print "Sending to Parse.com"
        handle.send()






try:
    with open("server.conf","r") as theConfig:
        x = json.loads(theConfig.read())
        watchFolder = x["folder"]
        parseAppId = x["X-Parse-Application-Id"]
        parseRESTKey = x["X-Parse-REST-API-Key"]


except IOError:
    print "Error Loading Config File"


if __name__ == '__main__':
    observer = Observer()
    observer.schedule(MyHandler(),path=watchFolder)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()