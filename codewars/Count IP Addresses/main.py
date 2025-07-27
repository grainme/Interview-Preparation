def ips_between(start, end):
    def ip_to_int(ip):
        ip = list(map(int, list(ip.split("."))[::-1]))
        print(ip)
        return ip[0] + (ip[1] << 8) + (ip[2] << 16) + (ip[3] << 24)
    return ip_to_int(end) - ip_to_int(start)
