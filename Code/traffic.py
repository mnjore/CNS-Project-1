import sys
import getopt
import time
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from os import popen
from scapy.all import sendp, IP, UDP, Ether, TCP
from random import randrange

# Generates random source ip addresses
def sourceIPgen():

    # These values are not valid for first octet of IP address
    invalid = [1,2,10,127,169,172,192,254]

    first = randrange(1,256)
    
    # This ensures the first value is a valid value
    while first in invalid:
        first = randrange(1,256)
    
    # Generating the other octets    
    second = randrange(1,256)
    third = randrange(1,256)
    fourth = randrange(1,256)
    
    # This joins together the ip address
    ip = ".".join([str(first),str(second),str(third),str(fourth)])

    return ip
    

# Generating the destination ip address
def gendest(foremost, last):

    # First three octets are the same for all addresses
    first = 10
    second = 0 
    third = 0
    fourth = randrange(foremost,last)
 
    # Joining together the ip address   
    ip = ".".join([str(first),str(second),str(third),str(fourth)])
    
    '''
    print(foremost)
    print(last)
    '''
    return ip
    
'''
if __name__ == '__main__':
  main()
'''

def main(argv):
    '''
    global foremost
    global last
    '''
    print(argv)
    try:
        opts, args = getopt.getopt(sys.argv[1:],'f:l:',['foremost','last='])
    # Exception handling
    except getopt.GetoptError:
        sys.exit(2)
        
    # This part takes in the specified values from the terminal
    for opt, arg in opts:
        if opt =='-f':
            foremost = int(arg)
        elif opt =='-l':
            last = int(arg)
            
    # This part terminates the program if the arguments are empty
    if foremost == '':
        sys.exit()
    if last == '':
        sys.exit()

    # This is to open the interface on the device to send out the packets
    interface = popen('ifconfig | awk \'/eth0/ {print $1}\'').read()

    # Packet generation
    for i in range(10000):
        packets = Ether()/IP(dst=gendest(foremost, last),src=sourceIPgen())/UDP(dport=80,sport=2)
        print(repr(packets))
        
        # Send packets every 0.05s
        sendp(packets,iface=interface.rstrip(),inter=0.05)


# Main
if __name__ == '__main__':
  main(sys.argv)