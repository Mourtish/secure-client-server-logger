# 🔐 Secure Client-Server Logger

A simple system design + cybersecurity project that demonstrates how a client communicates with a server using HTTP to send and store security logs.

---

## 📌 Overview

This project simulates a real-world logging system:

Client → sends log data → Server → processes → stores in file

It is designed to help understand:
- Client-server architecture
- HTTP communication
- REST APIs
- Basic logging systems (used in cybersecurity)

---

## 🧠 Core Concepts Explained

### 1. Client vs Server

- **Client**: A system that sends requests  
  Example: browser, script, mobile app  

- **Server**: A system that listens for requests and responds  

👉 In this project:
- Client = Python script sending logs
- Server = Flask app receiving logs

---

### 2. HTTP (HyperText Transfer Protocol)

HTTP is the protocol used for communication between client and server.

- **Request** → sent by client  
- **Response** → sent by server  

Example:
POST/LOG
---

### 3. API (Application Programming Interface)

An API is a way for systems to communicate.

This project uses a **REST API**:

| Endpoint | Method | Description |
|----------|--------|------------|
| /log     | POST   | Send log data |

---

### 4. JSON (JavaScript Object Notation)

A lightweight format for sending data.

Example:
```json
{
  "message": "Unauthorized login attempt"
}