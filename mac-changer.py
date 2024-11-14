from scapy.all import *

def get_interfaces():
    return [i for i in conf.iface]

def change_mac(interface, new_mac):
    sendp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.1.1", hwdst=new_mac), iface=interface, count=4)
    conf.iface = interface
    conf.verb = 0
    os.system("ifconfig %s down" % interface)
    os.system("ifconfig %s hw ether %s" % (interface, new_mac))
    os.system("ifconfig %s up" % interface)
    print(f"MAC address of {interface} changed to {new_mac}")

def main():
    interfaces = get_interfaces()
    if not interfaces:
        print("No interfaces found.")
        return

    print("Available interfaces:")
    for i in interfaces:
        print(i)

    interface = input("Enter the interface to change the MAC address of: ")
    if interface not in interfaces:
        print("Interface not found.")
        return

    new_mac = input("Enter the new MAC address (e.g., 00:11:22:33:44:55): ")

    change_mac(interface, new_mac)

if __name__ == "__main__":
    main()
