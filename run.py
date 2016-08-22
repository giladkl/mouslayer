import socket
port = 5000
s = socket. socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", port))
print "waiting on port:", port
first = True
while 1:
    data, addr = s.recvfrom(1024)
    if first:
    	x_firstx,y,z] =  data.split(",")