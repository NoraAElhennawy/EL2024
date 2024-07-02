import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
print(f"your ip is{ip}")
client.connect((ip,5000))

#while(True):
SMsg=str(input("Please enter your Msg"))
  #  SMsg=str(f"Msg{i} from client")
client.send(SMsg.encode("UTF-8"))
Rdata=client.recv(1024)
    #Faddr=str(Adrr)
print(f"{ip}  has sent you this Msg \n"+Rdata.decode('UTF-8'))
print("=====================================================")
client.close()