import sys
import socket
import threading
import encryption



def connect(conn):
    while True:
        received = conn.recv(1024)
        if received =='':
            pass
        else:
            msgr = received.decode()
            msgrd = crypt.decrypt(msgr)
            print("Them:  ",msgrd)

def sendMsg(conn):
    while True:
        send_msg = input()
        if send_msg == ' ':
            pass
        else:
            msgs = send_msg
            msgse = str(crypt.encrypt(msgs,rpubkey))[1:-1]
            sendthis = msgse.encode('utf-8')
            conn.sendall(sendthis)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: %s [port] " % sys.argv[0] )
        sys.exit(0)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', int(sys.argv[1])))

    print("choose encryption method")
    print("1.RSA")
    print("2.Random RSA")
    ch = int(input("enter final choice"))
    if ch == 1:
        p = int(input("enter a prime number \t"))
        q = int(input("enter another prime number \t"))
        crypt = encryption.RSA(p,q)
        print("your public key is ",crypt.public)
        rpubkey = input("enter public key to encode with(ie recievers public key)")
        if rpubkey.startswith('('):
            rpubkey = rpubkey[1:-1]
        rpubkey = rpubkey.split(',')
        rpubkey = (int(rpubkey[0]),int(rpubkey[1]))
    elif ch==2:
        crypt = encryption.RSA()
        print("your public key is ",crypt.public)
        rpubkey = input("enter public key to encode with(ie recievers public key)")
        if rpubkey.startswith('('):
            rpubkey = rpubkey[1:-1]
        rpubkey = rpubkey.split(',')
        rpubkey = (int(rpubkey[0]),int(rpubkey[1]))



    s.listen()
    (conn, addr) = s.accept() 
    print("initiating chat with client on",addr)
    thread1 = threading.Thread(target = connect, args = ([conn]))
    thread2 = threading.Thread(target = sendMsg, args = ([conn]))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
