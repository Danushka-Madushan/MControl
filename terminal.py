from flask import Flask
from extenstinos import controls

app = Flask(__name__)
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