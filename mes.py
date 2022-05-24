from binary import BinaryReader
import sys
import json
from pathlib import Path

path = open(sys.argv[1], "rb")
reader = BinaryReader(path.read())
if(reader.read_uint16()==3451):
    f = open(sys.argv[1], encoding='shift_jisx0213') # change it to "open file as text" (rather than initial binary) # might be a better way to do this than reopen the file
    fe = open(sys.argv[1] + ".DAT", "wb") # create or replace ("w") myfile.bin > name to sys.argv (compile)
    w = BinaryReader()
    w.set_endian(True)
    w.set_encoding("cp932")
    p = json.loads(f.read()) # load file to json
    nodecount = p["Count"]
    for i in range(nodecount):
        x = p[str(i)]
        txt = x["Line 1"]
        txt2 = x["Line 2"]
        txt3 = x["Line 3"]
        w.write_str_fixed_sjis(x["Line 1"],size = 48)
        w.write_str_fixed_sjis(x["Line 2"],size = 48)
        w.write_str_fixed_sjis(x["Line 3"],size = 48)
    print(txt.encode(encoding='cp932'))
    fe.write(w.buffer())
else:   
    filejson = open(sys.argv[1] + ".json","w",encoding='cp932')
    reader.seek(0)
    i = 0
    gay = dict()
    yes = Path(sys.argv[1]).stat().st_size
    test = yes/144
    num = int(test)
    header = {
        "Count": num
    }
    while i<num:
        x = {
            "Line 1" : reader.read_str(size=0x30, encoding='cp932'),
            "Line 2" : reader.read_str(size=0x30, encoding='cp932'),
            "Line 3" : reader.read_str(size=0x30, encoding='cp932'),
            }
        header.update({i: x})
        i+=1
    filejson.write(json.dumps(header,ensure_ascii = False, indent = 2))
