from flask import Flask, jsonify, request
from system import get_system_info, analyze_system, check_port

app = Flask(__name__)

# ---------------- TROUBLESHOOT FUNCTION ----------------
def troubleshoot_issue(user_input):
    user_input = user_input.lower()

    if "slow" in user_input:
        return "Your system may be slow due to high CPU/RAM usage."

    elif "cpu" in user_input:
        return "High CPU usage detected."

    elif "ram" in user_input or "memory" in user_input:
        return "High memory usage."

    elif "internet" in user_input or "network" in user_input:
        return "Check router/network settings."

    elif "virus" in user_input or "malware" in user_input:
        return "Run antivirus scan immediately."

    elif "battery" in user_input:
        return "Reduce brightness and background apps."

    else:
        return "Try restarting your system."


# ---------------- API ROUTES ----------------

@app.route("/")
def home():
    return jsonify({"message": "Cyber Security Assistant API Running"})


@app.route("/system-info")
def system_info():
    return jsonify(get_system_info())


@app.route("/analyze")
def analyze():
    return jsonify({
        "analysis": analyze_system()
    })


@app.route("/check-port/<int:port>")
def port_scan(port):
    return jsonify({
        "port": port,
        "status": check_port(port)
    })


@app.route("/troubleshoot", methods=["POST"])
def troubleshoot():

    data = request.get_json()

    issue = data.get("issue", "")

    solution = troubleshoot_issue(issue)

    return jsonify({
        "issue": issue,
        "solution": solution
    })


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)