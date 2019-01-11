import socket, os

#x = os.listdir("/users/lateefa/desktop/code/python code/filetransfer")

"""
    Run a for loop to do the function below for every file in the folder location
    given by variable x, which equals os.listdir().
        
"""

#SETS UP SERVER/HOST FOR CLIENTS TO CONNECT
s = socket.socket() #initailizes socket module
host = socket.gethostname() # finds the host's address
port = 8080 #port number for file distrubition
s.bind((host,port)) #binds the hostname and port to the server so the client can connect
s.listen(1) # listens for incoming connections, (1) is for 1 connection
print(host) #Prints hostname, type hostname in client
print("Waiting for any incoming connections....")
conn, addr = s.accept() # accepts any connections
print(addr, "Has connected to the server")

try:
    filename = raw_input(str("Please enter the filename of the file : "))
    file = open(filename, 'rb') #opens the file, permissions for file set to read
    file_data = file.read(1000000) #limits file size in bytes. Increase number to transfer bigger files
    conn.send(file_data) #actually transfers the file over port 8080
    print("Data has been transfered successfully")
except:
    print("Unable to transfer file")

