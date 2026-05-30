from flask import Flask, request, jsonify
import datetime
import time

app = Flask(__name__)

LOG_FILE = "../logs/logs.txt"

# 🔑 API KEY
API_KEY = "supersecretkey"

# ⏱️ RATE LIMIT SETTINGS
RATE_LIMIT = 5          # max requests
TIME_WINDOW = 60        # seconds

# 🧠 Store request timestamps per IP
request_log = {}


@app.route('/log', methods=['POST'])
def log():
    # 🔐 1. AUTHENTICATION
    client_api_key = request.headers.get("X-API-KEY")
    if client_api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    ip = request.remote_addr
    current_time = time.time()

    # ⏱️ 2. RATE LIMITING (TIME-BASED)
    if ip not in request_log:
        request_log[ip] = []

    # remove old requests outside time window
    request_log[ip] = [
        t for t in request_log[ip]
        if current_time - t < TIME_WINDOW
    ]

    if len(request_log[ip]) >= RATE_LIMIT:
        return jsonify({"error": "Too many requests"}), 429

    # add current request timestamp
    request_log[ip].append(current_time)

    # 📦 3. INPUT VALIDATION
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request"}), 400

    message = data.get("message")

    if not message.strip():
        return jsonify({"error": "Empty message"}), 400

    if len(message) > 200:
        return jsonify({"error": "Message too long"}), 400

    # 🕒 4. METADATA
    timestamp = datetime.datetime.now()

    log_entry = f"{timestamp} | {ip} | {message}\n"

    # 💾 5. STORE
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

    return jsonify({"status": "logged"}), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)