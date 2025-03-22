import sys
import threading
import time
import socket

print('-'*70)
print('Simple Port Scanner.')
print ('-'*70)

Ip_Domain=input('Enter Target IP OR Domain:')
print('_'*70)

try:
    target =socket.gethostbyname(Ip_Domain)
except socket.gaierror:
    print ('Name Resolution Error.')
    sys.exit()

start_port=int(input('Enter Start Port:'))
print('_'*70)
end_port=int(input('Enter End Port:'))
print ('_'*70)

portservices = {
    0: "Reserved",
    1: "TCP Port Service Multiplexer",
    5: "Remote Job Entry",
    7: "Echo",
    9: "Discard",
    11: "Active Users",
    13: "Daytime",
    17: "Quote of the Day",
    19: "Chargen",
    20: "FTP Data Transfer",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    37: "Time",
    53: "DNS",
    67: "DHCP (Server)",
    68: "DHCP (Client)",
    69: "TFTP",
    70: "Gopher",
    79: "Finger",
    80: "HTTP",
    81: "HTTP Alternate",
    82: "MIT ML Device",
    83: "MIT ML Device",
    88: "Kerberos",
    90: "DNSIX Securit Attribute Token Map",
    110: "POP3",
    111: "RPCbind",
    113: "Ident",
    115: "SFTP",
    119: "NNTP",
    123: "NTP",
    135: "MS RPC",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    163: "CMIP/TCP",
    164: "CMIP/TCP",
    179: "BGP",
    194: "IRC",
    199: "SMUX",
    200: "IBM 4758",
    201: "AppleTalk Routing Maintenance",
    204: "AT&T",
    210: "Z39.50",
    213: "IPX",
    220: "IMAP3",
    389: "LDAP",
    443: "HTTPS",
    445: "Microsoft-DS",
    464: "Kerberos Change/Set Password",
    465: "SMTP over SSL",
    514: "Syslog",
    515: "Printer",
    520: "RIP",
    521: "RIPng",
    523: "IBM",
    540: "UUCP",
    543: "Klogin",
    544: "KShell",
    548: "Apple Filing Protocol",
    554: "RTSP",
    563: "NNTPS",
    587: "SMTP (Submission)",
    631: "IPP (Internet Printing Protocol)",
    636: "LDAPS",
    639: "MSDP",
    646: "LDP",
    647: "DHCP Failover",
    651: "Reserved",
    666: "Doom",
}

def scan_port(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)
    conn =s.connect_ex((target,port))
    if (not conn):
        sercice=portservices.get(port,'Unknown Service')
        print ('Port {} is open.'.format(port),'(Services:{})'.format(sercice))
    s.close()

for port in range (start_port,end_port+1):
     thread=threading.Thread(target=scan_port,args=(port,)) 
     thread.start()   
print('Port scanning completed.')