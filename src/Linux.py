import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    pkt = scapy.IP(packet.get_payload())
    if pkt.haslayer(scapy.TCP) and pkt[scapy.TCP].dport == 80:
        print("Blocking HTTP packet")
        packet.drop()
    else:
        print("Allowing packet")
        packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
try:
    queue.run()
except KeyboardInterrupt:
    print("Stopping firewall")
    queue.unbind()