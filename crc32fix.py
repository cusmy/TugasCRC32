from array import array

poly = 0x04C11DB7

table = array('L')
for byte in range(256):
    crc = 0
    for bit in range(8):
        if (byte ^ crc) & 1:
            crc = (crc >> 1) ^ poly
        else:
            crc >>= 1
        byte >>= 1
    table.append(crc)

def hilih(string):
    value = 0xffffffff

    for mantap in string:
        value = table[((mantap) ^ value) & 0x000000ff] ^ (value >> 8)

    return value

hex = input("masukan Hex:").encode("utf-8")

print ("Hex Adalah:        0x%08x" % (hilih(hex)))
