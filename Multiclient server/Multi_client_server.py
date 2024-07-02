import socket
import threading
import time

#create server socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#get  My Ip and bind
ip=socket.gethostbyname(socket.gethostname())
print(f"your ip is{ip}")
s.bind((ip,5000))
s.listen(5)

def serv1():
    client,addr=s.accept()
    Rdata=client.recv(1024)
    print(f"{addr} with port  has sent you this Msg \n"+Rdata.decode('UTF-8'))
    print("=============================================================")
#    SMsg=str(input("Please enter your Msg for"+threading.current_thread().name))
    SMsg=f"Msg fro server{threading.current_thread().name}"
    client.send(SMsg.encode("UTF-8"))
    client.close()
    time.sleep(0.2)

def serv2():
    client2,addr2=s.accept()
    Rdata2=client2.recv(1024)
    print(f"{addr2} with port  has sent you this Msg \n"+Rdata2.decode('UTF-8'))
    print("=============================================================")
   # SMsg2=str(input("Please enter your Msg for "+threading.current_thread().name))
    SMsg2=f"Msg fro server{threading.current_thread().name}"  
    client2.send(SMsg2.encode("UTF-8"))
    client2.close()
    time.sleep(0.2)

def serv3():
    client3,addr3=s.accept()
    Rdata3=client3.recv(1024)
    print(f"{addr3} with port  has sent you this Msg \n"+Rdata3.decode('UTF-8'))
    print("=============================================================")
#    SMsg3=str(input("Please enter your Msg for "+threading.current_thread().name))
    SMsg3=f"Msg fro server{threading.current_thread().name}"  #  SMsg2="Msg fro server"
    client3.send(SMsg3.encode("UTF-8"))
    client3.close()
    time.sleep(0.2)

def serv4():
    client4,addr4=s.accept()
    Rdata4=client4.recv(1024)
    print(f"{addr4} with port  has sent you this Msg \n"+Rdata4.decode('UTF-8'))
    print("=============================================================")
#    SMsg4=str(input("Please enter your Msg for "+threading.current_thread().name))
  #  SMsg2="Msg fro server"
    SMsg4=f"Msg fro server{threading.current_thread().name}"
    client4.send(SMsg4.encode("UTF-8"))
    client4.close()
    time.sleep(0.2)
def serv5():
    client5,addr5=s.accept()
    Rdata5=client5.recv(1024)
    print(f"{addr5} with port  has sent you this Msg \n"+Rdata5.decode('UTF-8'))
    print("=============================================================")
#    SMsg5=str(input("Please enter your Msg for "+threading.current_thread().name))
  #  SMsg2="Msg fro server"
    SMsg5=f"Msg fro server{threading.current_thread().name}"
    client5.send(SMsg5.encode("UTF-8"))
    client5.close()
    time.sleep(0.2)

while(True):
    #create server threads
    s1=threading.Thread(target=serv1)
    s2=threading.Thread(target=serv2)
    s3=threading.Thread(target=serv3)
    s4=threading.Thread(target=serv4)
    s5=threading.Thread(target=serv5)
    #start threads
    s1.start()
    s2.start()
    s3.start()
    s4.start()
    s5.start()

    time.sleep(0.2)
    #wait till threads are done
    s1.join()
    s2.join()
    s3.join()
    s4.join()
    s5.join()
    print("done")