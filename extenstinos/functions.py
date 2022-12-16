from mss import mss
from time import time, ctime
import shutil, os

def screenshot():
	with mss() as sct:sct.shot()
	t = time()
	imgid = str(t).replace(".", "-")
	if not os.path.isdir('media'):
		os.system('mkdir media')
	shutil.move("monitor-1.png", "media/{}.png".format(imgid))
	return [imgid, ctime(t)]

def clean_ss():
	for each in os.listdir("media"):
		os.remove("media/%s" % each)
	return ["OK", "success"]

def shutdown():
	os.system('shutdown /s /t 30')
	return [30, "success"]

def abortshut():
	os.system('shutdown -a')
	return ["OK", "shutdown-aborted"]
