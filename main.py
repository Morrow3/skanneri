#tulostaa kytkimen ARP:in.
import arp
ip = "192.168.0."
i = 1
for i in range(0,24):
    vip = ip
    i +=1
    vip+=str(i)
    print vip
    dee = arp.arp_resolve(vip, strformat=False, source=None)
    #print dee
    print(arp.mac_straddr(dee, printable=True, delimiter=":"))
