from monitor.ping import monitor_hosts
from utils.config import HOSTS

if __name__ == "__main__":
    monitor_hosts(HOSTS)