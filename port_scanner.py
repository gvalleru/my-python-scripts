import socket

r_ip = raw_input("Whats the IP you want to do port scan? ")
print "=" * 40
print "Port scanning %s ........" %r_ip

for port in range(442,10000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #setting socket timeout to 0.5 secs which should be more than enough for tcp handshake
    #for most of the networks
    s.settimeout(0.5)
    result = s.connect_ex((r_ip, port))
    if result == 0:
        print "Port %s is open" %port



