queries = []
database = {}
import time
import subprocess
import socket
parent_ip = "128.110.96.132"
child_a = "128.110.96.131"
child_b = "128.110.96.136"
f = open('results.txt', 'w')


import socket
port = 5000
client_socket = socket.socket()
client_socket.connect((child_b, port))

# read the payload and store it in queries
filename = "payload.txt"
with open(filename) as file:
    for line in file:
        a = line.strip("\n").split(" ")
        queries += a
countt = len(queries)
loop = countt//2

# read the key-value pairs and store it in database
filename = "lookup_childA.txt"
with open(filename) as file:
    for line in file:
        a = line.strip("\n").split(" ")
        database[a[0]] = a[1]


i = 0

while i < loop:
    k = queries[2*i - 1]
    v = database.get(k)
    if v != None:
        if len(v) > 2:
            host_node = "child_b"
            t0 = time.perf_counter()
            client_socket.send(k.encode())
            data1 = client_socket.recv(1024).decode()
            #print(data1)
            t1 = time.perf_counter()
            f.write(str(((t1-t0)*1000))+"\n")
            print("Took " + str(((t1-t0)*1000)) + " milliseconds to GET " + k + " from " + host_node)
        else:
            host_node = "child_a"
            t0 = time.perf_counter()
            g = database.get(k)
            t1 = time.perf_counter()
            f.write(str(((t1-t0)*1000))+"\n")
            print("Took " + str(((t1-t0)*1000)) + " milliseconds to GET " + k + " from " + host_node)
    else:
        host_node = "parent"
        port = 5000
        t0 = time.perf_counter()
        client_socket_parent = socket.socket()  # instantiate
        client_socket_parent.connect((parent_ip, port))
        client_socket_parent.send(k.encode())
        data = client_socket_parent.recv(1024).decode()
        #print(data)
        if data != "!":
            #print(data)
            final = data.split(',')
            #print(str(final[0]) + " " + str(final[1]))
            #database["{0}".format(k)] = final[1]
        t1 = time.perf_counter()
        f.write(str(((t1-t0)*1000))+"\n")
        print("Took " + str(((t1-t0)*1000)) + " milliseconds to GET " + k + " from " + host_node)
        client_socket_parent.close()
    i+=1
f.close
