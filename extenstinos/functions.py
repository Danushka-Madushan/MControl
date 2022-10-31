from mss import mss
from time import time, ctime
import shutil

def screenshot():
	with mss() as sct:sct.shot()
	imgid = str(time()).replace(".", "-")
	shutil.move("monitor-1.png", "media/{}.png".format(imgid))
	return imgid

