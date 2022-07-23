queries = []
database = {}
import time
import subprocess
parent_ip = "128.110.96.132"
child_a = "128.110.96.131"
child_b = "128.110.96.136"

# read the payload and store it in queries
filename = "payload.txt"
with open(filename) as file:
    for line in file:
        a = line.strip("\n").split(" ")
        queries += a
countt = len(queries)
loop = queries/2

# read the key-value pairs and store it in database
filename = "lookup_childA.txt"
with open(filename) as file:
    for line in file:
        a = line.strip("\n").split(" ")
        database[a[0]] = a[1]

print(database)
fag = database.get("c")
print(fag)
i = 0

import socket

#host = socket.gethostname()  # as both code is running on same pc
port = 5000
client_socket = socket.socket()  # instantiate
client_socket.connect((parent_ip, port))  # connect to the server
message = input(" -> ")  # take input
while i < loop:
    k = queries[2*i - 1]
    if database.get(k) != 
    client_socket.send(queries[2*i - 1].encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response
    print('Received from server: ' + data)  # show in terminal
    message = input(" -> ")  # again take input

