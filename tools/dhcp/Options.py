from socket import inet_aton

# OPT NU : [TYPE,PARSE]
OPTION_LIST = {
2:["Time Offset", None],
3:["Router", None],
4:["Time Servers", None],
5:["Name Servers", None],
6:["DNS Servers", None],
7:["Log Servers", None],
8:["Cookie Servers", None],
9:["LPR Servers", None],
10:["Impress Servers", None],
11:["RLP Servers", None],
12:["Host Name", None],
13:["Boot File Size", None],
14:["Merit Dump File", None],
15:["Domain Name", None],
16:["Swap Server", inet_aton],
17:["Root Path", None],
18:["Extension File", None],
19:["IP Layer Forwarding", None],
20:["Src route enabler", None],
21:["Policy Filter", None],
22:["Maximum DG Reassembly Size", None],
23:["Default IP TTL", None],
24:["Path MTU Aging Timeout", None],
25:["MTU Plateau", None],
26:["Interface MTU Size", None],
27:["All Subnets Are Local", None],
28:["Broadcast Address", inet_aton],
29:["Perform Mask Discovery", None],
30:["Provide mask to others", None],
31:["Perform Router Discovery", None],
32:["Router Solicitation Address", inet_aton],
33:["Static Routing Table", None],
34:["Trailer Encapsulation", None],
35:["ARP Cache Timeout", None],
36:["Ethernet Encapsulation", None],
37:["Default TCP Time to Live", None],
38:["TCP Keepalive Interval", None],
39:["TCP Keepalive Garbage", None],
40:["NIS Domain Name", None],
41:["NIS Server Addresses", None],
42:["NTP Servers Addresses", None],
43:["Vendor Specific Information", None],
44:["NetBIOS Name Server", None],
45:["NetBIOS Datagram Distribution", None],
46:["NetBIOS Node Type", None],
47:["NetBIOS Scope", None],
48:["X Window Font Server", None],
49:["X Window Display Manager", None],
50:["Requested IP address", None],
51:["IP Address Lease Time", None],
52:["Option Overload", None],
53:["DHCP Message Type", None],
54:["DHCP Server Identification", None],
55:["Parameter Request List", None],
56:["Message", None],
57:["DHCP Maximum Message Size", None],
58:["Renew Time Value", None],
59:["Rebinding Time Value", None],
60:["Client Identifier", None],
61:["Client Identifier", None],
62:["Netware/IP Domain Name", None],
63:["Netware/IP sub Options", None],
64:["NIS+ V3 Client Domain Name", None],
65:["NIS+ V3 Server Address", None],
66:["TFTP Server Name", None],
67:["Boot File Name", None],
68:["Home Agent Addresses", None],
69:["Simple Mail Server Addresses", None],
70:["Post Office Server Addresses", None],
71:["Network News Server Addresses", None],
72:["WWW Server Addresses", None],
73:["Finger Server Addresses", None],
74:["Chat Server Addresses", None],
75:["StreetTalk Server Addresses", None],
76:["StreetTalk Directory Assistance Addresses", None],
77:["User Class Information", None],
78:["SLP Directory Agent", None],
79:["SLP Service Scope", None],
80:["Rapid Commit", None],
81:["FQDN, Fully Qualified Domain Name", None],
82:["Relay Agent Information", None],
83:["Internet Storage Name Service", None],
84:["Undefined", None],
85:["Novell Directory Servers", None],
86:["Novell Directory Server Tree Name", None],
87:["Novell Directory Server Context", None],
88:["BCMCS Controller Domain Name List", None],
89:["BCMCS Controller IPv4 Address List", None],
90:["Authentication", None],
91:["Undefined", None],92:["Undefined", None],
93:["Client System", None],
94:["Client Network Device Interface", None],
95:["LDAP Use", None],
96:["Undefined", None],
97:["UUID/GUID Based Client Identifier", None],
98:["Open Group's User Authentication", None],
99:["Undefined", None],100:["Undefined", None],101:["Undefined", None],
102:["Undefined", None],103:["Undefined", None],104:["Undefined", None],105:["Undefined", None],
106:["Undefined", None],107:["Undefined", None],108:["Undefined", None],
109:["Autonomous System Number", None],
110:["Undefined", None],111:["Undefined", None],
112:["NetInfo Parent Server Address", None],
113:["NetInfo Parent Server Tag", None],
114:["URL", None],
115:["Undefined", None],
116:["Auto Configure", None],
117:["Name Service Search", None],
118:["Subnet Collection", None],
119:["DNS Domain Search List", None],
120:["SIP Servers DHCP Option", None],
121:["Classless Static Route Option", None],
122:["CCC, CableLabs Client Configuration", None],
123:["GeoConf", None],
124:["Vendor-Identifying Vendor Class", None],
125:["Vendor Identifying Vendor Specific", None],
126:["Undefined", None],127:["Undefined", None],
128:["TFTP Server IP Address", None],
129:["Call Server IP Address", None],
130:["Discrimination String", None],
131:["Remote Statistics Server IP Address", None],
132:["802.1Q VLAN ID", None],
133:["802.1Q L2 Priority", None],
134:["Diffserv Code Point", None],
135:["HTTP Proxy For Phone Applications", None],
136:["Undefined", None],137:["Undefined", None],138:["Undefined", None],139:["Undefined", None],
140:["Undefined", None],141:["Undefined", None],142:["Undefined", None],143:["Undefined", None],
144:["Undefined", None],145:["Undefined", None],146:["Undefined", None],147:["Undefined", None],
148:["Undefined", None],149:["Undefined", None],
150:["TFTP Server Address, Etherboot, GRUB Config", None],
151:["Undefined", None],152:["Undefined", None],153:["Undefined", None],154:["Undefined", None],
155:["Undefined", None],156:["Undefined", None],157:["Undefined", None],158:["Undefined", None],
159:["Undefined", None],160:["Undefined", None],161:["Undefined", None],162:["Undefined", None],
163:["Undefined", None],164:["Undefined", None],165:["Undefined", None],166:["Undefined", None],
167:["Undefined", None],168:["Undefined", None],169:["Undefined", None],170:["Undefined", None],
171:["Undefined", None],172:["Undefined", None],173:["Undefined", None],174:["Undefined", None],
175:["Ether Boot", None],
176:["IP Telephone", None],
177:["Ether Boot PacketCable and CableHome", None],
178:["Undefined", None],179:["Undefined", None],180:["Undefined", None],181:["Undefined", None],182:["Undefined", None],
183:["Undefined", None],184:["Undefined", None],185:["Undefined", None],186:["Undefined", None],187:["Undefined", None],
188:["Undefined", None],189:["Undefined", None],190:["Undefined", None],191:["Undefined", None],192:["Undefined", None],
193:["Undefined", None],194:["Undefined", None],195:["Undefined", None],196:["Undefined", None],197:["Undefined", None],
198:["Undefined", None],199:["Undefined", None],200:["Undefined", None],201:["Undefined", None],202:["Undefined", None],
203:["Undefined", None],204:["Undefined", None],205:["Undefined", None],206:["Undefined", None],207:["Undefined", None],
208:["pxelinux.magic (string) = 241.0.116.126", None],
209:["pxelinux.configfile (text)", None],
210:["pxelinux.pathprefix (text)", None],
211:["pxelinux.reboottime", None],
212:["Undefined", None],213:["Undefined", None],214:["Undefined", None],215:["Undefined", None],
216:["Undefined", None],217:["Undefined", None],218:["Undefined", None],219:["Undefined", None],
220:["Subnet Allocation", None],
221:["Virtual Subnet Allocation", None],
222:["Undefined", None],223:["Undefined", None],
224:["Private Use", None],225:["Private Use", None],226:["Private Use", None],227:["Private Use", None],228:["Private Use", None],
229:["Private Use", None],230:["Private Use", None],231:["Private Use", None],232:["Private Use", None],233:["Private Use", None],
234:["Private Use", None],235:["Private Use", None],236:["Private Use", None],237:["Private Use", None],238:["Private Use", None],
239:["Private Use", None],240:["Private Use", None],241:["Private Use", None],242:["Private Use", None],243:["Private Use", None],
244:["Private Use", None],245:["Private Use", None],246:["Private Use", None],247:["Private Use", None],248:["Private Use", None],
249:["Private Use", None],250:["Private Use", None],251:["Private Use", None],252:["Private Use", None],253:["Private Use", None],
254:["Private Use", None]}