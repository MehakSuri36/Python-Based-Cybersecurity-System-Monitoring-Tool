from flask import Flask, request, jsonify
from system import get_system_info, analyze_system, check_port
import psutil
import os

app = Flask(__name__)

# ---------------- MALWARE PROCESS CHECK ----------------
def detect_suspicious_processes():

    suspicious = []

    try:

        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):

            try:

                cpu = proc.info['cpu_percent']
                name = proc.info['name']

                if cpu and cpu > 80:
                    suspicious.append(f"High CPU Usage: {name}")

                if name and any(x in name.lower() for x in ["temp", "crypt", "miner", "hack"]):
                    suspicious.append(f"Suspicious Name: {name}")

            except:
                pass

    except Exception as e:

        suspicious.append(f"Process scan unavailable: {str(e)}")

    return suspicious


# ---------------- NETWORK CONNECTION CHECK ----------------
def check_network_connections():

    suspicious_ports = []

    try:

        connections = psutil.net_connections()

        for conn in connections:

            if conn.laddr and conn.laddr.port not in [80, 443, 53]:
                suspicious_ports.append(conn.laddr.port)

    except Exception as e:

        return [f"Network scan unavailable: {str(e)}"]

    return list(set(suspicious_ports))[:10]


# ---------------- TOP CPU PROCESSES ----------------
def top_processes():

    procs = []

    try:

        for p in psutil.process_iter(['name', 'cpu_percent']):

            try:
                procs.append((p.info['name'], p.info['cpu_percent']))
            except:
                pass

        procs.sort(key=lambda x: x[1], reverse=True)

    except:
        pass

    return procs[:5]


# ---------------- STARTUP CHECK ----------------
def check_startup_items():

    try:

        if os.name == "nt":

            path = os.path.expanduser(
                "~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
            )

            return os.listdir(path)

        return ["Startup folder check not supported on Linux"]

    except:
        return []


# ---------------- COMMON PORT SCAN ----------------
def scan_common_ports():

    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389, 8080]

    results = {}

    for port in common_ports:

        try:
            results[port] = check_port(port)

        except:
            results[port] = "Error"

    return results


# ---------------- MALWARE ANALYSIS ----------------
def malware_scan():

    processes = detect_suspicious_processes()

    ports = check_network_connections()

    startup = check_startup_items()

    top = top_processes()

    risk = 0

    if processes:
        risk += 2

    if ports:
        risk += 1

    if len(startup) > 5:
        risk += 1

    response = "\n🔍 ===== ADVANCED MALWARE SCAN =====\n"

    response += "\n🧪 Scan Type: Behavioral + Heuristic"

    response += "\n🔐 Mode: Threat Detection\n"

    # Suspicious Processes
    response += "\n⚠️ Suspicious Processes:\n"

    if processes:

        for p in processes:
            response += f"\n- {p}"

    else:
        response += "\n- None detected"

    # Ports
    response += "\n\n🌐 Unusual Open Ports:\n"

    if ports:
        response += str(ports)

    else:
        response += "None"

    # CPU Processes
    response += "\n\n🔥 Top CPU Processes:\n"

    for name, cpu in top:
        response += f"\n- {name}: {cpu}%"

    # Startup
    response += "\n\n📂 Startup Items:\n"

    if startup:

        for item in startup:
            response += f"\n- {item}"

    else:
        response += "\nNone"

    # Infection Sources
    response += "\n\n🧠 Possible Infection Sources:\n"

    sources = [
        "Downloaded executable files",
        "Email attachments",
        "USB devices",
        "Malicious websites"
    ]

    for s in sources:
        response += f"\n- {s}"

    # Security Report
    response += "\n\n🧠 ===== SECURITY REPORT =====\n"

    if risk >= 3:

        response += "\n🔴 RISK LEVEL: HIGH"
        response += "\n⚠️ Strong indicators of malicious activity"

    elif risk == 2:

        response += "\n🟡 RISK LEVEL: MEDIUM"
        response += "\n⚠️ Some suspicious behavior detected"

    else:

        response += "\n🟢 RISK LEVEL: LOW"
        response += "\n✅ No strong indicators detected"

    # Remedies
    response += "\n\n🛠 Recommended Actions:\n"

    fixes = [
        "Disconnect from internet",
        "End suspicious processes",
        "Delete unknown files",
        "Run antivirus scan",
        "Update system",
        "Avoid unknown downloads"
    ]

    for r in fixes:
        response += f"\n- {r}"

    return response


# ---------------- HELP MENU ----------------
def help_menu():

    return """
🛡 CYBER SECURITY ASSISTANT

Available Features:

1️⃣ System Information
Examples:
• show system info
• pc information
• device details

2️⃣ System Analysis
Examples:
• analyze system
• check pc health
• system health

3️⃣ Port Scan
Examples:
• scan ports
• open ports
• network scan

4️⃣ Malware Scan
Examples:
• scan my system
• malware analysis
• security scan
• virus check

5️⃣ Full System Check
Examples:
• full system check
• complete scan
• analyze everything

6️⃣ Performance Issues
Examples:
• system is slow
• laptop hanging
"""


# ---------------- CHATBOT RESPONSE ----------------
def chatbot_response(message):

    message = message.lower()

    # HELP
    if any(x in message for x in [
        "help",
        "menu",
        "commands",
        "options"
    ]):

        return help_menu()

    # SYSTEM INFO
    elif any(x in message for x in [
        "system info",
        "information",
        "pc info",
        "show system",
        "device info"
    ]):

        info = get_system_info()

        return f"""
📊 SYSTEM INFORMATION

💻 OS: {info['OS']}
🔥 CPU Usage: {info['CPU']}%
🧠 RAM Usage: {info['RAM']}%
"""

    # ANALYZE SYSTEM
    elif any(x in message for x in [
        "analyze",
        "health",
        "system health",
        "analyze system",
        "check system"
    ]):

        return f"""
📈 SYSTEM ANALYSIS

{analyze_system()}
"""

    # PORT SCAN
    elif any(x in message for x in [
        "port",
        "scan ports",
        "open ports",
        "network scan"
    ]):

        ports = scan_common_ports()

        response = "\n🌐 COMMON PORT SCAN\n"

        for port, status in ports.items():
            response += f"\nPort {port}: {status}"

        return response

    # MALWARE SCAN
    elif any(x in message for x in [
        "malware",
        "virus",
        "scan my system",
        "scan pc",
        "security scan",
        "infected",
        "hack"
    ]):

        return malware_scan()

    # FULL SYSTEM CHECK
    elif any(x in message for x in [
        "full check",
        "complete scan",
        "check everything",
        "full system check",
        "analyze everything"
    ]):

        info = get_system_info()

        response = f"""
⚙️ ===== FULL SYSTEM CHECK =====

📊 SYSTEM INFORMATION

💻 OS: {info['OS']}
🔥 CPU Usage: {info['CPU']}%
🧠 RAM Usage: {info['RAM']}%

📈 SYSTEM ANALYSIS

{analyze_system()}
"""

        response += "\n\n🌐 COMMON PORT SCAN\n"

        ports = scan_common_ports()

        for port, status in ports.items():
            response += f"\nPort {port}: {status}"

        response += "\n\n"

        response += malware_scan()

        return response

    # PERFORMANCE ISSUES
    elif any(x in message for x in [
        "slow",
        "lag",
        "freeze",
        "hanging",
        "performance"
    ]):

        return """
⚠️ PERFORMANCE ISSUE DETECTED

Suggestions:

• Restart your system
• Close background applications
• Check RAM usage
• Run malware scan
• Update operating system
"""

    # DEFAULT
    else:

        return help_menu()


# ---------------- API ----------------
@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()

        message = data.get("message", "")

        response = chatbot_response(message)

        return jsonify({
            "reply": response
        })

    except Exception as e:

        return jsonify({
            "reply": f"Error occurred: {str(e)}"
        })


# ---------------- HOME ----------------
@app.route("/")
def home():

    return "Cyber Security Chatbot Running"


# ---------------- RUN ----------------
if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
