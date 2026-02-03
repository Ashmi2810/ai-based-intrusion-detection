from scapy.all import sniff
import csv
from datetime import datetime

file = open("traffic.csv", "w", newline="")
writer = csv.writer(file)

# ADD timestamp to header
writer.writerow([
    "timestamp",
    "src_ip",
    "dst_ip",
    "protocol",
    "src_port",
    "dst_port",
    "length"
])

def collect(packet):
    if packet.haslayer("IP"):
        timestamp = datetime.now()   # timestamp PER packet

        src = packet["IP"].src
        dst = packet["IP"].dst
        length = len(packet)

        if packet.haslayer("TCP"):
            protocol = "TCP"
            sport = packet["TCP"].sport
            dport = packet["TCP"].dport

        elif packet.haslayer("UDP"):
            protocol = "UDP"
            sport = packet["UDP"].sport
            dport = packet["UDP"].dport

        else:
            protocol = "OTHER"
            sport = 0
            dport = 0

        # WRITE timestamp with packet data
        writer.writerow([
            timestamp,
            src,
            dst,
            protocol,
            sport,
            dport,
            length
        ])

sniff(count=1000, prn=collect)

file.close()
