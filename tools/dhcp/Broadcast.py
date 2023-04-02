from socket import inet_aton
from tools.dhcp.Message import Message


def decode(byte_msg):

    msg = Message()
    
    # To find the byte offsets and more details about the 
    # data look here.
    # http://www.tcpipguide.com/free/t_DHCPMessageFormat.htm
    # https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol

    msg._OP = byte_msg[0]
    msg._HTYPE = byte_msg[1]
    msg._HLEN = byte_msg[2]
    msg._HOPS = byte_msg[3]
    msg._XID = byte_msg[4:8]
    msg._SECS = byte_msg[8:10]
    msg._FLAGS = byte_msg[10:12]
    msg._CIADDR = byte_msg[12:16]
    msg._YIADDR = byte_msg[16:20]
    msg._SIADDR = byte_msg[20:24]
    msg._GIADDR = byte_msg[24:28]
    
    # Offset now depends on data length.
    offset = 28 + msg.HLEN

    msg._CHADDR = byte_msg[28:offset]

    offset += 10 # CHADDR is followed by 10 byte padding.
    
    msg._SNAME = byte_msg[offset: offset+64]
    offset += 64 # Advance the offset.

    msg._FILE = byte_msg[offset:offset+128]
    offset += 128 # Advance the offset.

    msg._MAGIC_COOKIE = byte_msg[offset:offset+4]
    offset += 4 # Advance the offset.

    opts = {}
    while True:
        # Break free if true
        if offset >= len(byte_msg):
            break

        # One byte containing option type number
        opt_type = byte_msg[offset:offset+1]

        offset += 1 # Advance the offset.

        # Number 255 means end of options
        if opt_type == 255:
            break

        # Option lengh, how long the data portion of the option is.
        opt_len = int.from_bytes(byte_msg[offset:offset+1], "big")
        offset += 1 # Advance the offset.

        # Option data
        opt_data = byte_msg[offset:offset + opt_len]
        offset += opt_len

        opts.update({opt_type: opt_data})

    msg._OPTIONS = opts
    a = msg.options()
    return msg

def encode(data):
    return data