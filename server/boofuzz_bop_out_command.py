from boofuzz import *


host = "192.168.0.231"
port = 3260
proto = "tcp"

session = Session(
    target=Target(
        connection=SocketConnection(host, port, proto)
    )
)

s_initialize("iSCSI NOP OUT")
s_byte(0x40,fuzzable=False)  # OP_CODE NOP-Out
s_bytes(value=b'\x80\x00\x00', size=3,fuzzable=True)  # RESERVED
s_byte(0x00,fuzzable=True)  # Total AHS Length
s_bytes(value=b'\x00\x00\x00', size=3,fuzzable=True)  # length
s_bytes(value=b'\x00\x00\x00\x00\x00\x00\x00\x00', size=8,fuzzable=True)  # LUNs
s_bytes(value=b'\x15\x00\x00\x00', size=4,fuzzable=True)  # Initiator Task Tag
s_bytes(value=b'\xff\xff\xff\xff', size=4,fuzzable=True)  # Target transfer Tag
s_bytes(value=b'\x00\x00\x02\x00', size=4,fuzzable=True)  # CmdSN
s_bytes(value=b'\x00\x00\x02\x90', size=4,fuzzable=True)  # Expect stat SN
s_bytes(value=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', size=16,fuzzable=True)  # Command Descriptor Block (CDB) Read

session.connect(s_get("iSCSI NOP OUT"))
session.fuzz()
