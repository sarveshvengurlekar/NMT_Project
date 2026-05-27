from scapy.all import sniff, IP, TCP, UDP, ICMP

packet_count = 0

def analyze_packet(packet):
    global packet_count
    packet_count += 1

    print(f"\n📦 Packet #{packet_count}")

    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")

        if packet.haslayer(TCP):
            print("Protocol: TCP")
        elif packet.haslayer(UDP):
            print("Protocol: UDP")
        elif packet.haslayer(ICMP):
            print("Protocol: ICMP")
        else:
            print("Protocol: Other")

# Start sniffing
print("🚀 Starting Packet Capture... Press CTRL+C to stop")
sniff(prn=analyze_packet, store=False)