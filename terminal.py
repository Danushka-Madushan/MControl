from flask import Flask, jsonify, request, send_from_directory, render_template
from extenstinos import Admin, Execute, Validate, DeviceID

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./media"

@app.route('/', methods=["GET"])
def main():
	return render_template("index.html")

@app.route('/execute', methods=['POST'])
def execute():
	data = request.json
	response = jsonify({"status":"success", "info":Execute(data['command']).get_data()})
	return response, 200

@app.route("/media/<path:name>/<token>", methods=['GET'])
def download_file(name, token):
	name = "%s.png" % name
	if Validate(token).check():
		return send_from_directory(app.config['UPLOAD_FOLDER'], name)
	else:
		return {"status":"failed", "reason":"Invalid token"}

# Login System
# Make a Web interface that can control users pc with buttons and commands
# Ex: there is a button called Shutdown When you pushed that button yout pc will shut down
# Requirements : Pc and the mobile device must be in same network

# Features
	# Shutdown
	# Sleep
	# Sleep ++
	# Take a Screenshot of PC
	# Run Specific Command
	
# Login System

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
