# from datetime import datetime

# def log_event(message):
#     with open("logs/network.log", "a", encoding="utf-8") as f:
#         f.write(f"{datetime.now()} - {message}\n")

from datetime import datetime

def log_event(message, level="INFO", host=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_line = f"[{timestamp}] [{level}]"

    if host:
        log_line += f" [{host}]"

    log_line += f" {message}"

    with open("logs/network.log", "a", encoding="utf-8") as f:
        f.write(log_line + "\n")