from socket import *
import argparse

def AddParse():
    # parse_object = optparse.OptionParser(usage="If you want scan just one port you can ( python3 main.py -n <site.com> -p <port> )")
    # parse_object.add_option("-n","--name",dest="tgtHosts",help="Ping scanning!")
    # parse_object.add_option("-p","--ports",dest="tgtPorts",help="Scanning Port!",type=str)

    parser = argparse.ArgumentParser( prog= 'PortScanner', 
                            description="If you want scan ports you can ( python3 main.py -n <site.com> -p <port,port> )",
                            epilog='-p: You can select ports -n: Which domain scan are you want'
                            )
    parser.add_argument('-n', "--name", dest="Hosts")
    parser.add_argument('-p', "--port", dest="Ports", type=int,nargs='+')
    
    return parser.parse_args()

def conScan(tgtHost,tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost,tgtPort))
        print('[+]%s/tcp open'% tgtPort)
        connskt.close()
    except:
        print('[-]%s/tcp close'% tgtPort)
        
        
        
def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
        print('[+] Server ip: %s'% tgtIP)
    except:
        print('[-] Cannot resolve %s'% tgtHost)
        return
    
    setdefaulttimeout(1)

    for port in tgtPorts:
        print('[?] Scanning Port: %s'% port)
        conScan(tgtHost,port)
        
if __name__ == '__main__':
    portScan(AddParse().Hosts,AddParse().Ports)
    