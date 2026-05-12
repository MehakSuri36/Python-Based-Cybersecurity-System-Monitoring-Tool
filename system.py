import platform
import socket

try:
    import psutil
    _PSUTIL_AVAILABLE = True
except ImportError:
    psutil = None
    _PSUTIL_AVAILABLE = False


def get_system_info():
    info = {
        "OS": platform.system()
    }

    if not _PSUTIL_AVAILABLE:
        info["CPU"] = "psutil not installed"
        info["RAM"] = "psutil not installed"
        return info

    info["CPU"] = psutil.cpu_percent()
    info["RAM"] = psutil.virtual_memory().percent
    return info


def analyze_system():
    if not _PSUTIL_AVAILABLE:
        return "psutil not installed; system usage unavailable"

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    if cpu > 80:
        return "High CPU usage"
    elif ram > 80:
        return "High RAM usage"
    else:
        return "System is running fine"


def check_port(port):
    s = socket.socket()
    result = s.connect_ex(('127.0.0.1', port))
    return "OPEN" if result == 0 else "CLOSED"


if __name__ == "__main__":
    print("System Information:")
    for key, value in get_system_info().items():
        print(f"{key}: {value}")

    print("\nSystem Analysis:")
    print(analyze_system())
