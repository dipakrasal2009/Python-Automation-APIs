import subprocess
from flask import Flask

app = Flask(__name__)

@app.route("/DockerLaunch/<dockerimage>/<dockername>")
def docker_launch(dockerimage, dockername):
    # Validate and sanitize user input before using it in the command
    if not valid_input(dockername) or not valid_input(dockerimage):
        return "Invalid input"

    cmd = f"docker run -i -t -d --name {dockername} {dockerimage}"
    
    try:
        cid = subprocess.check_output(cmd, shell=True, text=True)
        return f"Docker Launch Successfully : {cid}"
    except subprocess.CalledProcessError as e:
        return f"Error launching Docker container: {e}"

@app.route("/stop/<dockername>")
def docker_stop(dockername):
    # Validate and sanitize user input before using it in the command
    if not valid_input(dockername):
        return "Invalid input"

    cmd = f"docker stop {dockername}"
    
    try:
        subprocess.check_output(cmd, shell=True)
        return "Docker stopped"
    except subprocess.CalledProcessError as e:
        return f"Error stopping Docker container: {e}"

def valid_input(input_str):
    # Implement your validation logic here
    return input_str.isalnum()  # Example validation - checks if input is alphanumeric

if __name__ == "__main__":
    app.run()
