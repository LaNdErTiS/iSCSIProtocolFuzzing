from boofuzz import *


host = "192.168.0.231"
port = 3260
proto = "tcp"

session = Session(
    target=Target(
        connection=SocketConnection(host, port, proto)
    )
)

s_initialize("scsi command Read")
s_byte(0x01,fuzzable=False)  # OP_CODE SCSI Command Read
s_byte(0xc1,fuzzable=True)  # Flags and Task Attributes
s_bytes(value=b'\x00\x00', size=2,fuzzable=True)  # RESERVED
s_byte(0x00,fuzzable=True)  # Total AHS Length
s_bytes(value=b'\x00\x00\x00', size=3,fuzzable=True)  # length
s_bytes(value=b'\x00\x01\x00\x00\x00\x00\x00\x00', size=8,fuzzable=True)  # LUNs
s_bytes(value=b'\x3a\x00\x00\x00', size=4,fuzzable=True)  # Initiator Task Tag
s_bytes(value=b'\x00\x00\x10\x00', size=4,fuzzable=True)  # Expected Data Transfer Length
s_bytes(value=b'\x00\x00\x00\x39', size=4,fuzzable=True)  # CmdSN
s_bytes(value=b'\x00\x00\x00\x3a', size=4,fuzzable=True)  # Expect stat SN
s_bytes(value=b'\x28\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', size=16,fuzzable=True)  # Command Descriptor Block (CDB) Read

session.connect(s_get("scsi command Read"))
session.fuzz()
