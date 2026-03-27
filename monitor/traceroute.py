import subprocess

def run_traceroute(host):
    print(f"Running traceroute for {host}...\n")

    result = subprocess.run(
        ["tracert", host],
        capture_output=True,
        text=True
    )

    print(result.stdout)