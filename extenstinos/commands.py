from extenstinos import functions

func = {
	"ss": "screenshot"
}

funcrtn = {
	"ss": ["Screenshot/png", "media_id"]
}

class execute():
	def __init__(self, arg):
		self.arg = arg
		self.data = getattr(functions, func[arg])()
	
	def get_data(self):
		return {"data":funcrtn[self.arg][0], funcrtn[self.arg][1]:self.data}
