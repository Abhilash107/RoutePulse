import subprocess
import time
from utils.config import LATENCY_THRESHOLD, PING_INTERVAL
from monitor.traceroute import run_traceroute
from utils.logger import log_event


def ping(host):
    result = subprocess.run(
        ["ping", "-n", "1", host],
        capture_output=True,
        text=True
    )
    output = result.stdout.lower()

    if "time=" in output:
        latency_str = output.split("time=")[-1].split("ms")[0]
        latency = float(latency_str)
        return latency
    return None


# def monitor_hosts(hosts):
    while True:
        for host in hosts:
            latency = ping(host)

            if latency:
                print(f"{host}: {latency} ms")

                if latency > LATENCY_THRESHOLD:
                    alert_msg = f"⚠️ High latency: {latency} ms ({host})"
                    print(alert_msg)

                    log_event(alert_msg)
                    run_traceroute(host)
        #print("DEBUG:", PING_INTERVAL, type(PING_INTERVAL))
        time.sleep(PING_INTERVAL)


def monitor_hosts(hosts):
    while True:
        for host in hosts:
            latency = ping(host)

            if latency is not None:
                print(f"{host}: {latency} ms")

                # Log normal metric
                log_event(
                    f"Latency: {latency} ms",
                    level="INFO",
                    host=host
                )

                if latency > LATENCY_THRESHOLD:
                    alert_msg = f"High latency: {latency} ms"
                    
                    print(f"⚠️ {alert_msg} ({host})")

                    log_event(
                        alert_msg,
                        level="WARNING",
                        host=host
                    )

                    run_traceroute(host)

            else:
                # Handle ping failure
                print(f"{host}: Ping failed")

                log_event(
                    "Ping failed",
                    level="ERROR",
                    host=host
                )

        time.sleep(PING_INTERVAL)