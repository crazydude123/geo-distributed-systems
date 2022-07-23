queries = []
database = {}
parent_ip = "128.110.96.132"
child_a = "128.110.96.131"
child_b = "128.110.96.136"
import socket

# read the payload and store it in queries
filename = "payload.txt"
with open(filename) as file:
    for line in file:
        a = line.strip("\n").split(" ")
        queries += a

# read the key-value pairs and store it in database
filename = "lookup_childB.txt"
with open(filename) as file:
    for line in file:
        a = line.strip("\n").split(" ")
        database[a[0]] = a[1]

print(database)
fag = database.get("c")
print(fag)

def server_program():
    host = child_b
    port = 5000

    server_socket = socket.socket()  
    server_socket.bind((host, port))

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        answer = database.get(str(data))
        print(answer)
        conn.send(answer.encode())  # send data to the client
if __name__ == '__main__':
    server_program()
