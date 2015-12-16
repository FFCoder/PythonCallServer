import json
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from models import *

watchFolder = ""

class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.wav","*.mp3"]


    def on_created(self, event):
        x = Call(open(event.src_path))





try:
    with open("server.conf","r") as theConfig:
        x = json.loads(theConfig.read())
        watchFolder = x["folder"]


except IOError:
    print "Error Loading Config File"
    watchFolder = "."

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