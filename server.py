from flask import Flask
import subprocess
from verification import startdb

app = Flask(__name__)


@app.route("/payload", methods=['POST', 'GET'])
def git_pull():
    p = subprocess.Popen(['git', 'pull'], cwd='/home/smarthome')
    p.wait()
    return "Done!"


@app.route("/reboot", methods=["GET"])
def reboot_system():
    subprocess.Popen(["sudo", "reboot"])
    return "Das Gerät wird neu gestartet!"


@app.route("/startVerify", methods=["POST"])
def start_verification():
    return "Verification satrted"


@app.route("/verify", methods=["GET"])
def verify_user():
    return "User is now verified"


@app.route("/testDB")
def test_db():
    subprocess.Popen(['python3', '/home/smarthome/verification/testdb.py'])
    return startdb.db


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
