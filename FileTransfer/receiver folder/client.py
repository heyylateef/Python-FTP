import socket

#CONNECTS CLIENT TO SERVER 
s = socket.socket() #initializes socket module
host = raw_input(str("Please enter the host address of the sender: "))
port = 8080 #port number for file distribution
s.connect((host,port)) # connecets to host by the typed hostname
print("Connected....")

filename = raw_input(str("Please enter a filename for the incoming file: "))

try:
    file = open(filename, 'wb') # opens the file, permissions for the file set to write
    file_data = s.recv(1000000) #limits the received file size in bytes. Increase the number to receive bigger files
    file.write(file_data)
    file.close()
    print("File has been received successfully.")
except:
    print("Unable to receive file")
