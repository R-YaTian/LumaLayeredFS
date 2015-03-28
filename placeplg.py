import os,struct

def mkdir(path):
                isExists=os.path.exists(path)
                if not isExists:
                                os.makedirs(path)
                                return True
                else:
                                return False

exh = open('workdir\\exheader.bin','rb')
exh.seek(512)
lid = str(hex(struct.unpack('I',exh.read(4))[0]))[2:]
hid = str(hex(struct.unpack('I',exh.read(4))[0]))[2:]
if len(lid)<8:
                lid = '0'*(8-len(lid))+lid
if len(hid)<8:
                hid = '0'*(8-len(hid))+hid
jumpid = hid+lid
mkdir('workdir\\plugin\\'+jumpid)
plg = open('workdir\\layeredfs.plg','rb')
data = plg.read()
plgo = open('workdir\\plugin\\'+jumpid+'\\layeredfs.plg','wb')
plgo.write(data)
plg.close()
plgo.close()
os.remove('workdir\\layeredfs.plg')
