from flask import Flask
from flask import render_template
from Utils import robot 
    
app = Flask(__name__)

@app.route("/")
def home():
    ret = []
    for key in robot.getLogKeys():
        ret.append((key, robot.getLog(key)))
    return render_template('logs.html', logs=ret)

@app.route("/add/<key>/<log>")
def add(key, log):
    robot.putLog(key, log)
    return home()

if __name__ == '__main__':
   app.run(debug = True)