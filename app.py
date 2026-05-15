from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
  return f"""
  Hello World <br>
  Server: {socket.gethostname()}<br>
  PID: {os.getpid()}
  """
