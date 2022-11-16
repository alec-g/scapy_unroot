#! /usr/bin/env python


from scapy_unroot import configure_sockets
from scapy.all import sniff

configure_sockets()

if __name__ == "__main__":
  packets = sniff(filter="host %s" % ('google.com'), count=5)
  print(packets)