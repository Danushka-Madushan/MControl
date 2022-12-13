from mss import mss
from time import time, ctime
import shutil, os

def screenshot():
	with mss() as sct:sct.shot()
	t = time()
	imgid = str(t).replace(".", "-")
	shutil.move("monitor-1.png", "media/{}.png".format(imgid))
	return [imgid, ctime(t)]

def clean_ss():
	for each in os.listdir("media"):
		os.remove("media/%s" % each)
	return [None, "success"]
