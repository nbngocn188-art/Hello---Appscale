from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return f"""
  Hello World <br>
  Server: {socket.gethostname()}<br>
  PID: {os.getpid()}
  """
