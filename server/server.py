from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

LOG_FILE = "../logs/logs.txt"

@app.route('/log', methods=['POST'])
def log():
    data = request.json
    message = data.get("message")

    timestamp = datetime.datetime.now()
    ip = request.remote_addr
    log_entry = f"{timestamp} | {ip} | {message}\n"


    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

    return jsonify({"status": "logged"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
