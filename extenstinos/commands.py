from extenstinos import functions

func = {
	"ss": "screenshot",
	"ss-clear": "clean_ss"
}

funcrtn = {
	"ss": ["Screenshot/png", "media_id", "stamp"],
	"ss-clear": ["None", "None", "status"]
}

class Execute():
	def __init__(self, arg):
		self.arg = arg
		self.data = getattr(functions, func[arg])()
	
	def get_data(self):
		return {"data":funcrtn[self.arg][0], funcrtn[self.arg][1]:self.data[0], funcrtn[self.arg][2]:self.data[1]}
