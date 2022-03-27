from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/payload", methods=['POST'])
def gitHubUpdate():
    p = subprocess.Popen(['git','pull'], cwd='/home/smarthome')
    p.wait()
    return "Done!"

@app.route("/reboot", methods=["GET"])
def rebootSystem():
    subprocess.Popen(["sudo", "reboot"])
    return "Das Gerät wird neu gestartet!"

@app.route("/startVerify", methods=["POST"])
def startVerification():
    return "Verification satrted"

@app.route("/verify", methods=["GET"])
def verifyUser():
    return "User is now verified"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)