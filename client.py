import sys
import socket
import threading
import encryption


crypt = encryption.RSA()

def connect(s):
    while True:
        r_msg = s.recv(1024)
        if not r_msg:
            break
        if r_msg == '':
            pass
        else:
            msgr = r_msg.decode()
            msgrd = crypt.decrypt(msgr)
            print("Them:  ",msgrd)

def receive(s):
    while True:
        s_msg = input()
        if s_msg == '':
            pass
        else:
            msgs = s_msg
            msgse = str(crypt.encrypt(msgs,rpubkey))[1:-1]
            sendthis = msgse.encode('utf-8')
            s.sendall(sendthis)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage: %s [ip adress][port] " % sys.argv[0] )
        sys.exit(0)

    print("choose encryption method")
    print("1.RSA")
    print("2.Random RSA")
    ch = int(input("enter final choice"))
    if ch == 1:
        p = int(input("enter a prime number \t"))
        q = int(input("enter another prime number \t"))
        crypt = encryption.RSA(p,q)
        print("your public key is ",crypt.public)
        rpubkey = input("enter public key to encode with (ie recievers public key)")
        if rpubkey.startswith('('):
            rpubkey = rpubkey[1:-1]
        rpubkey = rpubkey.split(',')
        rpubkey = (int(rpubkey[0]),int(rpubkey[1]))
    elif ch==2:
        crypt = encryption.RSA()
        print("your public key is ",crypt.public)
        rpubkey = input("enter public key to encode with (ie recievers public key)")
        if rpubkey.startswith('('):
            rpubkey = rpubkey[1:-1]
        rpubkey = rpubkey.split(',')
        rpubkey = (int(rpubkey[0]),int(rpubkey[1]))


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((sys.argv[1], int(sys.argv[2])))
    print("initiating Chat with server on ", sys.argv[1])
    thread1 = threading.Thread(target = connect, args = ([s]))
    thread2 = threading.Thread(target = receive, args = ([s]))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
