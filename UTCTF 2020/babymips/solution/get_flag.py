s = [0x62, 0x6c, 0x7f, 0x76, 0x7a, 0x7b, 0x66, 0x73, 0x76, 0x50, 0x52, 0x7d, 0x40, 0x54, 0x55, 0x79, 0x40, 0x49, 0x47, 0x4d, 0x74, 0x19, 0x7b, 0x6a, 0x42, 0xa,
     0x4f, 0x52, 0x7d, 0x69, 0x4f, 0x53, 0xc, 0x64, 0x10, 0xf, 0x1e, 0x4a, 0x67, 0x3, 0x7c, 0x67, 0x2, 0x6a, 0x31, 0x67, 0x61, 0x37, 0x7a, 0x62, 0x2c, 0x2c,
     0xf, 0x6e, 0x17, 0, 0x16, 0xf, 0x16, 0xa, 0x6d, 0x62, 0x73, 0x25, 0x39, 0x76, 0x2e, 0x1c, 0x63, 0x78, 0x2b, 0x74, 0x32, 0x16, 0x20, 0x22, 0x44, 0x19]
flag = ''

for i in range(0, len(s)):
    flag += chr(s[i] ^ i + 0x17)

print(flag)