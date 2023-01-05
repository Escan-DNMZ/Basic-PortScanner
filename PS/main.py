from socket import *

def conScan(tgtHost,tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost,tgtPort))
        print('[+]%d/tcp open'% tgtPort)
        connskt.close()
    except:
        print('[-]%d/tcp close'% tgtPort)
        
        
        
def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
        print('[+] Server ip: %s'% tgtIP)
    except:
        print('[-] Cannot resolve %s'% tgtHost)
        return
    
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('[?] Scanning Port: %d'% tgtPort)
        conScan(tgtHost,int(tgtPort))
        
if __name__ == '__main__':
    domainName = input("Which site do you ping: ")
    Ports = []
    Adet = input("How many ports do you want to enter: ")
    girdi = 0
    while girdi < int(Adet):
        girdi +=1   
        Port = input("Which port scan do you want: ")
        Ports.append(int(Port))

    portScan(domainName,Ports)