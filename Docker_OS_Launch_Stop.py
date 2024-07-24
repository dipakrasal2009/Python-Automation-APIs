import subprocess
from flask import Flask

app = Flask(__name__)

@app.route("/DockerLaunch/<dockerimage>/<dockername>")
def docker_launch(dockerimage,dockername):

    cmd = f"docker run --name {dockername} -i -t -d {dockerimage}"

    cid = subprocess.getoutput(cmd)

    return f"Docker Launch Successfully : {cid}"


@app.route("/stop/<dockername>")
def docker_stop(dockername):
    cmd = f"docker stop {dockername}"

    subprocess.getoutput(cmd)

    return "Docker stopped"


app.run(port=80,host="0.0.0.0")





