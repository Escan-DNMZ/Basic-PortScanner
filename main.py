from socket import *
import optparse

def AddParse():
    parse_object = optparse.OptionParser(usage="If you want scan just one port you can ( python3 main.py -n <site.com> -p <port> )")
    parse_object.add_option("-n","--name",dest="tgtHosts",help="Ping scanning!")
    parse_object.add_option("-p","--ports",dest="tgtPorts",help="Scanning Port!",type=str)

    return parse_object.parse_args()

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

    
    print('[?] Scanning Port: %s'% tgtPorts)
    conScan(tgtHost,int(tgtPorts))
        
if __name__ == '__main__':
    (user_input, arguments) = AddParse()
    
        
    portScan(user_input.tgtHosts,user_input.tgtPorts)
 