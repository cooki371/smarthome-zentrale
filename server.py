from flask import Flask
import subprocess
from verification import verification

app = Flask(__name__)


@app.route("/payload", methods=['POST', 'GET'])
def git_pull():
    p = subprocess.Popen(['git', 'pull'], cwd='/home/pi/smarthome')
    p.wait()
    return "Done!"


@app.route("/reboot", methods=["GET"])
def reboot_system():
    subprocess.Popen(["sudo", "reboot"])
    return "Das Gerät wird neu gestartet!"


@app.route("/startVerify/<mail>", methods=["POST", "GET"])
def start_verification(mail):
    verification.startVerify(mail)
    return "Verification satrted"


@app.route("/verify", methods=["GET"])
def verify_user():
    return "User is now verified"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
