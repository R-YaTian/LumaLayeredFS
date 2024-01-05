import filecmp
import os
import shutil
import struct


def walk(dirname):
    filelist = []
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            fullname = os.path.join(root, filename)
            filelist.append(fullname)
    return filelist


def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False


def getid():
    exh = open('workdir\\exh.bin', 'rb')
    exh.seek(512)
    lid = str(hex(struct.unpack('I', exh.read(4))[0]))[2:]
    hid = str(hex(struct.unpack('I', exh.read(4))[0]))[2:]
    lid = '0' * (8 - len(lid)) + lid
    hid = '0' * (8 - len(hid)) + hid
    jumpid = hid + lid
    return jumpid


filePath = 'luma/titles/'
filePath = filePath + getid() + '/romfs'

if not os.path.exists('workdir\\romfs1'):
    os.system("3dstool -xtf romfs workdir\\romfs1.bin --romfs-dir workdir\\romfs1")
if not os.path.exists('workdir\\romfs2'):
    os.system("3dstool -xtf romfs workdir\\romfs2.bin --romfs-dir workdir\\romfs2")
if not (os.path.exists('workdir\\romfs1') or os.path.exists('workdir\\romfs2')):
    exit()

dir1 = 'workdir\\romfs1'
dir2 = 'workdir\\romfs2'
dirout = 'workdir\\' + filePath.replace('/', '\\')
mkdir(dirout)
filelist1 = walk(dir1)
filelist2 = walk(dir2)

for filename in filelist2:
    if filename.replace(dir2, dir1) in filelist1:
        compareresult = filecmp.cmp(filename.replace(dir2, dir1), filename)
        if not compareresult:
            outfilename = filename.replace(dir2, dirout)
            mkdir(os.path.split(outfilename)[0])
            shutil.copy(filename, outfilename)
            print('Copy: ', outfilename)
    elif not filename.replace(dir2, dir1) in filelist1:
        outfilename = filename.replace(dir2, dirout)
        mkdir(os.path.split(outfilename)[0])
        shutil.copy(filename, outfilename)
        print('Copy: ', outfilename)
