class PingResult:
    def __init__(self, host, latency, status):
        self.host = host
        self.latency = latency
        self.status = status