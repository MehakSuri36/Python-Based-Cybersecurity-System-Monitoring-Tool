A Python-based all-in-one cybersecurity diagnostic tool that helps analyze system health, detect suspicious activity, scan network ports, and troubleshoot system issues using a smart rule-based engine.

This project simulates a lightweight Security Operations Assistant (SOC tool) for personal system analysis and learning purposes.

🚀 Features
🖥 System Monitoring
Fetch system information
Analyze system performance
Monitor CPU-intensive processes
Check startup applications
🌐 Port Scanner
Scan common attack-prone ports
Perform full port scan (1–1024)
Check specific port status
Detect open suspicious ports
🦠 Malware Analysis
Detect suspicious processes (CPU spikes, keywords)
Identify unusual network connections
Analyze startup entries
Generate risk level (Low / Medium / High)
🧠 Smart Issue Diagnostic System
Accepts user-described system problems
Identifies possible cause categories:
Network issues
Performance issues
Malware infections
Hardware failures
Provides:
Root causes
Step-by-step fixes
Prevention strategies
⚙ Full System Security Check
System info + analysis
Common port scan integration
Malware behavior analysis
Overall system risk evaluation
🧠 How It Works

This tool uses a rule-based decision system:

Keyword detection for issue classification
System process monitoring via psutil
Network socket scanning using socket
Heuristic-based malware detection
Predefined security response models

It behaves like a lightweight offline cybersecurity assistant.

🛠 Technologies Used
Python 3.x
psutil (system monitoring)
socket (network scanning)
os module (system interaction)
