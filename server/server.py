from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

LOG_FILE = "../logs/logs.txt"

# 🔑 Secret API Key (server side)
API_KEY = "supersecretkey"

@app.route('/log', methods=['POST'])
def log():
    # 🔐 1. AUTHENTICATION CHECK
    client_api_key = request.headers.get("X-API-KEY")

    if client_api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    # 📦 2. INPUT VALIDATION
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request"}), 400

    message = data.get("message")
    # 🚫 3. PREVENT EMPTY LOGS
    if not message.strip():
        return jsonify({"error": "Empty message"}), 400

    # 📏 4. LIMIT MESSAGE LENGTH
    if len(message) > 200:
        return jsonify({"error": "Message too long"}), 400

    # 🕒 3. ADD METADATA
    timestamp = datetime.datetime.now()
    ip = request.remote_addr

    log_entry = f"{timestamp} | {ip} | {message}\n"

    # 💾 4. STORE LOG
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

    return jsonify({"status": "logged"}), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)