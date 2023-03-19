from boofuzz import *


host = "192.168.0.231"
port = 3260
proto = "tcp"

session = Session(
    target=Target(
        connection=SocketConnection(host, port, proto)
    )
)

s_initialize("Log out")
s_byte(0x46,fuzzable=False)  # OP_CODE NOP-Out
s_byte(0x80,fuzzable=False)  # Reason
s_bytes(value=b'\x00\x00', size=2,fuzzable=True)  # RESERVED
s_byte(0x00,fuzzable=True)  # Total AHS Length
s_bytes(value=b'\x00\x00\x00', size=3,fuzzable=True)  # length
s_bytes(value=b'\x00\x00\x00\x00\x00\x00\x00\x00', size=8,fuzzable=True)  # RESERVED
s_bytes(value=b'\x2b\x00\x00\x00', size=4,fuzzable=True)  # Initiator Task Tag
s_bytes(value=b'\x00\x00', size=2,fuzzable=True)  # CID
s_bytes(value=b'\x00\x00', size=2,fuzzable=True)  # RESERVED
s_bytes(value=b'\x00\x00\x00\x67', size=4,fuzzable=True)  # CmdSN
s_bytes(value=b'\x00\x00\x00\xaa', size=4,fuzzable=True)  # Expect stat SN
s_bytes(value=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', size=16,fuzzable=True)  # Command Descriptor Block (CDB) Read

session.connect(s_get("Log out"))
session.fuzz()
