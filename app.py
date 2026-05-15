from flask import Flask
import os

app = Flask(__name__)

@app.router('/')
def home():
  return f"Hello World from {os.getenv('RAILWAY_REPLICA_ID')}"
app.run(host='0.0.0.0', port=8080)
