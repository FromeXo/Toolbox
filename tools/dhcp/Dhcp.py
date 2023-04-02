import socket
import tools.dhcp.Scanner
from tools.dhcp.Client import Client
import os
import sys
import tools.dhcp.Broadcast as broadcast

class Dhcp:

    NAME = "Dhcp"
    DESC = "You are the dhcp server."
    VERS = "1.0.0"

    def main():
        
        res = (b"\x01\x01\x06\x00q\x885@\x18}\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb8'\xeb\x11N\xfb\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00c\x82Sc5\x01\x01=\x07\x01\xb8'\xeb\x11N\xfbP\x00t\x01\x019\x02\x05\xc0\x0c\x04leaf\x91\x01\x017\x0e\x01y!\x03\x06\x0c\x0f\x1a\x1c36:;w\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", ('0.0.0.0', 68))
        #client = Client(res)
        #print(client.__dict__)
        try:

            msg = broadcast.decode(res[0])
            print(msg.options())
        except Exception as e:
            print(e)
        return False

        print("DHCP - Be your own server!\n")

        print("Listen to specific ip?")
        bindTo = input("Bind: ")
        if len(bindTo) == 0:
            bindTo = ""

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        if os.geteuid() > 0:
            print("Must be ROOT to bind socket")
            return False
                    
        try:
            s.bind((bindTo, 67))
            print("Socket binding operation completed")    
        except Exception as e:
            print(e)

      

        #except Exception as e:
        #    print(e.code)
        #    print(e)

        
        
        print("Start broadcast discovery")
        test = s.recvfrom(300)
        


        input()

        return False

    
if __name__ == "__main__":
    Dhcp.main()