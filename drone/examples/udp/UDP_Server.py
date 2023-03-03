import socket

SERVER_IP     = "0.0.0.0"
SERVER_PORT   = 20001
BUFFER_SIZE   = 1024

msgFromServer = "Hello UDP Client"
bytesToSend   = str.encode(msgFromServer)

# Create a datagram socket
serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
serverSocket.bind((SERVER_IP, SERVER_PORT))
print("UDP server launched successfully. Listening...")

# Listen for incoming datagrams
while(True):
    bytesAddressPair = serverSocket.recvfrom(BUFFER_SIZE)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    serverSocket.sendto(bytesToSend, address)