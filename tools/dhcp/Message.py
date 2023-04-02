from base64 import b16encode
from socket import inet_ntoa, inet_aton

def pack_str(data):
    return data

def unpack_str(data):
    return data

def pack_num(num):
    return num

def unpack_num(num, order="big"):
    return int.from_bytes(num, order)
#
def pack_none(ret):
    return ret

def unpack_none(ret):
    return ret
#
def unpack_mac(mac_bytes):
    return ":".join('%02x' % ord(b) for b in mac_bytes)

def pack_mac(mac_string):
    s = b16encode(mac_string)
    return ':'.join([s[i:i+2].decode('ascii') for i in range(0, 12, 2)])
#OPTIONS_LIST = (
# ["Pad", pack_none, unpack_none],
# ["Subnet Mask", inet_ntoa, inet_aton],
# ["time Offset", pack_num, unpack_num]
# )


MESSAGE_TYPES = {
    1 : "DHCPDISCOVER",
    2 : "DHCPOFFER",
    3 : "DHCPREQUEST",
    4 : "DHCPDECLINE",
    5 : "DHCPACK",
    6 : "DHCPNAK",
    7 : "DHCPRELEASE",
    8 : "DHCPINFORM"
}
def byte_to_message_type(b):
    i = int.from_bytes(b, "big")
    return MESSAGE_TYPES[i]

def ntoaX(ips):
    print(ips)
    return b''.join(map(inet_aton, ips))

def byte_to_ascii(x):
    return x.decode("ASCII")

def byte_to_int(b, order="big"):
    return int.from_bytes(b, order)
def byte_to_mac(mac_in_byte):
    hex = b16encode(mac_in_byte)
    ret = "{}:{}:{}:{}:{}".format(
        hex[0:2].decode("ascii"),
        hex[2:4].decode("ascii"),
        hex[4:6].decode("ascii"),
        hex[8:10].decode("ascii"),
        hex[10:12].decode("ascii"))
    return ret
# List of DHCP options and how to handle them.
# https://www.iana.org/assignments/bootp-dhcp-parameters/bootp-dhcp-parameters.xhtml
OPTIONS_LIST = {
    0:["Pad", None],
    1:["Subnet Mask", inet_ntoa],
    2:["Time Offset", byte_to_int],
    3:["Router", ntoaX],
    4:["Time Servers", ntoaX],
    5:["Name Servers", ntoaX],
    6:["DNS Servers", list],
    7:["Log Servers", ntoaX],
    8:["Cookie Servers", ntoaX],
    9:["LPR Servers", ntoaX],
    10:["Impress Servers", ntoaX],
    11:["RLP Servers", None],
    12:["Host Name", byte_to_ascii],
    13:["Boot File Size", byte_to_int],
    14:["Merit Dump File", None],
    15:["Domain Name", ntoaX],
    16:["Swap Server", inet_aton],17:["Root Path", None],18:["Extension File", None],19:["IP Layer Forwarding", None],20:["Src route enabler", None],21:["Policy Filter", None],22:["Maximum DG Reassembly Size", None],23:["Default IP TTL", None],24:["Path MTU Aging Timeout", None],25:["MTU Plateau", None],26:["Interface MTU Size", None],27:["All Subnets Are Local", None],28:["Broadcast Address", inet_aton],29:["Perform Mask Discovery", None],30:["Provide mask to others", None],31:["Perform Router Discovery", None],32:["Router Solicitation Address", inet_aton],
    33:["Static Routing Table", None],34:["Trailer Encapsulation", None],35:["ARP Cache Timeout", None],36:["Ethernet Encapsulation", None],37:["Default TCP Time to Live", None],38:["TCP Keepalive Interval", None],39:["TCP Keepalive Garbage", None],40:["NIS Domain Name", None],41:["NIS Server Addresses", None],42:["NTP Servers Addresses", None],43:["Vendor Specific Information", None],44:["NetBIOS Name Server", None],45:["NetBIOS Datagram Distribution", None],46:["NetBIOS Node Type", None],47:["NetBIOS Scope", None],48:["X Window Font Server", None],49:["X Window Display Manager", None],50:["Requested IP address", None],51:["IP Address Lease Time", None],52:["Option Overload", None],53:["DHCP Message Type", byte_to_message_type],54:["DHCP Server Identification", None],
    55:["Parameter Request List", list],56:["Message", None],
    57:["DHCP Maximum Message Size", byte_to_int],58:["Renew Time Value", None],59:["Rebinding Time Value", None],60:["Client Identifier", None],
    61:["Client Identifier", byte_to_mac],62:["Netware/IP Domain Name", None],63:["Netware/IP sub Options", None],64:["NIS+ V3 Client Domain Name", None],65:["NIS+ V3 Server Address", None],66:["TFTP Server Name", None],67:["Boot File Name", None],68:["Home Agent Addresses", None],69:["Simple Mail Server Addresses", None],70:["Post Office Server Addresses", None],71:["Network News Server Addresses", None],72:["WWW Server Addresses", None],73:["Finger Server Addresses", None],74:["Chat Server Addresses", None],75:["StreetTalk Server Addresses", None],76:["StreetTalk Directory Assistance Addresses", None],77:["User Class Information", None],78:["SLP Directory Agent", None],79:["SLP Service Scope", None],
    80:["Rapid Commit", ntoaX],81:["FQDN, Fully Qualified Domain Name", None],82:["Relay Agent Information", None],83:["Internet Storage Name Service", None],84:["Undefined", None],85:["Novell Directory Servers", None],86:["Novell Directory Server Tree Name", None],87:["Novell Directory Server Context", None],88:["BCMCS Controller Domain Name List", None],89:["BCMCS Controller IPv4 Address List", None],90:["Authentication", None],91:["Undefined", None],92:["Undefined", None],93:["Client System", None],94:["Client Network Device Interface", None],95:["LDAP Use", None],96:["Undefined", None],97:["UUID/GUID Based Client Identifier", None],98:["Open Group's User Authentication", None],99:["Undefined", None],100:["Undefined", None],101:["Undefined", None],102:["Undefined", None],103:["Undefined", None],104:["Undefined", None],105:["Undefined", None],106:["Undefined", None],107:["Undefined", None],108:["Undefined", None],109:["Autonomous System Number", None],110:["Undefined", None],111:["Undefined", None],112:["NetInfo Parent Server Address", None],113:["NetInfo Parent Server Tag", None],114:["URL", None],115:["Undefined", None],
    116:["Auto Configure", byte_to_int],117:["Name Service Search", None],118:["Subnet Collection", None],119:["DNS Domain Search List", None],120:["SIP Servers DHCP Option", None],
    121:["Classless Static Route Option", None],122:["CCC, CableLabs Client Configuration", None],123:["GeoConf", None],124:["Vendor-Identifying Vendor Class", None],125:["Vendor Identifying Vendor Specific", None],126:["Undefined", None],127:["Undefined", None],128:["TFTP Server IP Address", None],129:["Call Server IP Address", None],130:["Discrimination String", None],131:["Remote Statistics Server IP Address", None],132:["802.1Q VLAN ID", None],133:["802.1Q L2 Priority", None],134:["Diffserv Code Point", None],135:["HTTP Proxy For Phone Applications", None],136:["Undefined", None],137:["Undefined", None],138:["Undefined", None],139:["Undefined", None],140:["Undefined", None],141:["Undefined", None],142:["Undefined", None],143:["Undefined", None],144:["Undefined", None],
    145:["Undefined", None],146:["Undefined", None],147:["Undefined", None],148:["Undefined", None],149:["Undefined", None],150:["TFTP Server Address, Etherboot, GRUB Config", None],151:["Undefined", None],152:["Undefined", None],153:["Undefined", None],154:["Undefined", None],155:["Undefined", None],156:["Undefined", None],157:["Undefined", None],158:["Undefined", None],159:["Undefined", None],160:["Undefined", None],161:["Undefined", None],162:["Undefined", None],163:["Undefined", None],164:["Undefined", None],165:["Undefined", None],166:["Undefined", None],167:["Undefined", None],168:["Undefined", None],169:["Undefined", None],170:["Undefined", None],171:["Undefined", None],172:["Undefined", None],173:["Undefined", None],174:["Undefined", None],175:["Ether Boot", None],176:["IP Telephone", None],177:["Ether Boot PacketCable and CableHome", None],178:["Undefined", None],179:["Undefined", None],180:["Undefined", None],181:["Undefined", None],182:["Undefined", None],183:["Undefined", None],184:["Undefined", None],185:["Undefined", None],186:["Undefined", None],187:["Undefined", None],188:["Undefined", None],189:["Undefined", None],190:["Undefined", None],191:["Undefined", None],192:["Undefined", None],193:["Undefined", None],194:["Undefined", None],195:["Undefined", None],196:["Undefined", None],197:["Undefined", None],198:["Undefined", None],199:["Undefined", None],200:["Undefined", None],201:["Undefined", None],202:["Undefined", None],203:["Undefined", None],204:["Undefined", None],205:["Undefined", None],206:["Undefined", None],207:["Undefined", None],208:["pxelinux.magic (string) = 241.0.116.126", None],209:["pxelinux.configfile (text)", None],210:["pxelinux.pathprefix (text)", None],211:["pxelinux.reboottime", None],212:["Undefined", None],213:["Undefined", None],214:["Undefined", None],215:["Undefined", None],216:["Undefined", None],217:["Undefined", None],218:["Undefined", None],219:["Undefined", None],220:["Subnet Allocation", None],221:["Virtual Subnet Allocation", None],222:["Undefined", None],223:["Undefined", None],224:["Private Use", None],225:["Private Use", None],226:["Private Use", None],227:["Private Use", None],228:["Private Use", None],229:["Private Use", None],230:["Private Use", None],231:["Private Use", None],232:["Private Use", None],233:["Private Use", None],234:["Private Use", None],235:["Private Use", None],236:["Private Use", None],237:["Private Use", None],238:["Private Use", None],239:["Private Use", None],240:["Private Use", None],241:["Private Use", None],242:["Private Use", None],243:["Private Use", None],244:["Private Use", None],245:["Private Use", None],246:["Private Use", None],247:["Private Use", None],248:["Private Use", None],249:["Private Use", None],250:["Private Use", None],251:["Private Use", None],252:["Private Use", None],253:["Private Use", None],254:["Private Use", None]}


class Message:

    # Operation Code
    # Specifies the general type of message.
    # 1: Request message, 2: Reply message
    _OP = None

    @property
    def OP(self):
        return self._OP
    
    def operation_code(self):
        if self._op == 1:
            return "Request Message"
        elif self._op == 2:
            return "Replay Message"
        else:
            raise ValueError("Operation Code value is not in range.")

    # Hardware Type: Specifies the type of hardware used for the local network.
    _HTYPE = None
    @property
    def HTYPE(self):
        return self._HTYPE
    
    def hardware_type(self):
        types = {
            1: "Ethernet 10mb",
            6: "IEEE 802 Networks",
            7: "ARCNET",
            11: "LocalTalk",
            12: "LocalNet",
            14: "SMDS",
            15: "Frame Relay",
            15: "Async Transfer Mode",
            17: "HDLC",
            18: "Fibre Channel",
            19: "Async Transfer Mode",
            20: "Serial Line"}
        if self._HTYPE in types.keys():
            return types[self._HTYPE]
        else:
            raise ValueError("Hardware Type value is not in range.")

    # Hardware Address Length
    # Specifies how long hardware addresses are in this message.
    # For Ethernet or other networks using IEEE 802 MAC addresses, the value is 6.
    _HLEN = None
    @property
    def HLEN(self):
        return self._HLEN

    def hardware_address_length(self):
        return self._HLEN
    
    # Hops: Set to 0 by a client before transmitting a request.
    # Used by relay agents to control the forwarding of BOOTP and/or DHCP messages.
    _HOPS = None
    @property
    def HOPS(self):
        return self._HOPS

    def hops(self):
        return self._HOPS

    # Transaction Identifier: A 32-bit identification field generated by the client.
    # To allow it to match up the request with replies received from DHCP servers.
    _XID = None
    @property
    def XID(self):
        return self._XID
    
    def transaction_identifier(self):
        return int.from_bytes(self._XID, "big")

    # Seconds: The number of seconds elapsed since a client began an attempt to acquire or renew a lease.
    # This may be used by a busy DHCP server to prioritize replies when multiple client requests are outstanding.
    _SECS = None
    @property
    def SECS(self):
        return self._XID
    
    def seconds(self):
        return int.from_bytes(self._XID, "big")

    # Flags
    _FLAGS = None
    @property
    def FLAGS(self):
        return self._FLAGS
    
    # Client IP Address
    _CIADDR = None
    @property
    def CIADDR(self):
        return self._CIADDR
    
    def client_ip(self):
        return inet_ntoa(self._CIADDR)
        
    # “Your” IP Address: The IP address that the server is assigning to the client.
    _YIADDR = None
    @property
    def YIADDR(self):
        return self._YIADDR

    def your_ip_address(self):
        return inet_ntoa(self._YIADDR)
    
    # Server IP Address: The address of the server that the client should use for the next step in the bootstrap process,
    # which may or may not be the server sending this reply.
    _SIADDR = None
    @property
    def SIADDR(self):
        return self._SIADDR
    
    def server_ip_address(self):
        return inet_ntoa(self._SIADDR)
    
    # Gateway IP Address
    # This field is not used by clients and does not represent the server giving the client the address of a default router
    _GIADDR = None
    @property
    def GIADDR(self):
        return self._GIADDR
    
    def gateway_ip_address(self):
        return inet_ntoa(self._GIADDR)
    
    # Client Hardware Address: The hardware (layer two) address of the client
    _CHADDR = None
    @property
    def CHADDR(self):
        return self._CHADDR

    def client_hardware_address(self):
        return byte_to_mac(self._CHADDR)

    # Server Name: The server sending a DHCPOFFER or DHCPACK message
    _SNAME = None
    @property
    def SNAME(self):
        return self._SNAME
    
    def server_name(self):
        return self._SNAME.decode("ascii")

    # Boot Filename: Optionally used by a client to request a particular type of boot file in a DHCPDISCOVER message.
    # Used by a server in a DHCPOFFER to fully specify a boot file directory path and filename.
    _FILE = None
    @property
    def FILE(self):
        return self._FILE
    
    def file(self):
        file = b16encode(self._FILE)
        file.decode('ASCII')
        return file

    # Magic Cookie
    # Used to identify the information as vendor-independent option fields.
    _MAGIC_COOKIE = None
    @property
    def MAGIC_COOKIE(self):
        return self._MAGIC_COOKIE
    
    def magic_cookie(self):
        return inet_ntoa(self._MAGIC_COOKIE)
    
    # Options: Holds DHCP options, including several parameters required for basic DHCP operation.
    _OPTIONS = None
    @property
    def OPTIONS(self):
        return self._OPTIONS
    
    def options(self):
        options = {}
        #options.update({
        #        OPTIONS_LIST[opt[0]][0]: OPTIONS_LIST[opt[0]][1](opt[1])
        #    })

        for opt in self._OPTIONS:
            i = int.from_bytes(opt, "big")
            v = self._OPTIONS[opt]
            if i in OPTIONS_LIST and OPTIONS_LIST[i][1] is not None:
                options.update({i : OPTIONS_LIST[i][1](v)})
        return options


    def __init__(self, type=0):
        self.type = type


