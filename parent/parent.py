import socket
database = {}
parent_ip = "128.110.96.132"
child_a = "128.110.96.131"
child_b = "128.110.96.136"
none = "None"

# read the database and store it in RAM
filename = "lookup_parent.txt"
with open(filename) as file:
    for line in file:
        a = line.strip("\n").split(" ")
        database[a[0]] = a[1]



def server_program():
    host = parent_ip
    port = 5000

    server_socket = socket.socket()  
    server_socket.bind((host, port))

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
      # accept new connection
    #print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        conn, address = server_socket.accept()
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        answer = str(database.get(str(data)))
        if answer != "None":
            print(answer)
            conn.send(answer.encode())
        else:
            conn.send("{0}".format("!").encode()) 
        # send data to the client
if __name__ == '__main__':
    server_program()