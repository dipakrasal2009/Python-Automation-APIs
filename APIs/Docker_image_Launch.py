import subprocess
from flask import Flask

app = Flask(__name__)

@app.route("/DockerLaunch/<dockername>/<dockerimage>")
def docker_launch(dockername,dockerimage):

    cmd = f"docker run -it -d --name {dockername} {dockerimage}"

    cid = subprocess.getoutput(cmd)

    return f"Docker Launch Successfully : {cid}"


@app.route("/stop/<dockername>")
def docker_stop(dockername):
    cmd = f"docker stop {dockername}"

    subprocess.getoutput(cmd)

    return "Docker stopped"


app.run()
