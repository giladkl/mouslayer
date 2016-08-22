import socket, position_proccesser

if __name__ == "__main__":
	port = 5000
	s = socket. socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(("0.0.0.0", port))
	print "waiting on port:", port
	first = True
	pattern = "%.4f"

	while 1:
		data, addr = s.recvfrom(1024)
		if "L" == data:
			print "yay"
		else:
			force = [round(float(i), 2) for i in data.split(",")]

			if first:

				pos_proccesser = position_proccesser.PositionProccesser(force)
				first = False

			else:
				print pos_proccesser.calculate_movement_from_force(data[0], data[1])