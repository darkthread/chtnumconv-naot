import ctypes
chtnumconverter = ctypes.cdll.LoadLibrary("X:/Github/chtnumconv-naot/bin/Release/net8.0/win-x64/native/chtnumconv-naot.dll")
s = '一千零二十四'
n = chtnumconverter.parse_cht_num(s.encode('utf-8'))
print(n)
chtnumconverter.to_cht_num.restype = ctypes.c_char_p
p = chtnumconverter.to_cht_num(65536) # p = pointer to string
# TODO 找出回傳 UTF-8 編碼的方法
print(p.decode('big5'))
chtnumconverter.free_mem(p); # free memory