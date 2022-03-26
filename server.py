from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/payload", methods=['POST'])
def gitHubUpdate():
    p = subprocess.Popen(['git','pull'], cwd='/home/smarthome')
    p.wait()

    return "Done!"

if __name__ == "__main__":
    app.run(host='localhost', port=80)