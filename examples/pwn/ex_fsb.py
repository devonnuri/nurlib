#!/usr/bin/env python
from ptrlib import *

# Assume:
# - 32 bits
# - We have printf(buf)
# - The contents of buf appears at the 6th position on the stack
#   printf("%6$p") = 0x70243625
# - We want to write 0xdeadbeef to 0xcafebabe, 0xfee1dead to 0xba5eba11
writes = {
    0xcafebabe: 0xdeadbeef,
    0xba5eba11: 0xfee1dead
}
payload = fsb(
    6, writes, bs=1, bits=32
)
print(payload)

# Assume:
# - 64 bits
# - We have printf("Result: " + buf)
# - The contents of ("Result: " + buf) appears at the 7th position on the stack
#   printf("%7%p") = 0x70253625203a746c
# - We want to write 0xabcd to 0x7fffcafebabe
# - Note that we can't write several values at once because of the NULL bytes
writes = {
    0x7fffcafebabe: 0xabcd
}
payload = fsb(
    7, writes, bs=2, bits=64, written=8
)
print(payload)
